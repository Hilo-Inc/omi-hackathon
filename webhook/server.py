"""
Bilingual Conversation Coach - Real-time Webhook Server
Receives live transcripts from Omi and returns translations + follow-up suggestions.
"""

import os
import httpx
import uuid
import re
import json
from datetime import datetime, timedelta
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, Response, HTMLResponse
from pydantic import BaseModel
from typing import Optional
import openai
from prompts import REALTIME_SYSTEM_PROMPT

# Initialize
app = FastAPI(title="Bilingual Conversation Coach")
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# TTS Configuration
KOKORO_TTS_URL = os.getenv("KOKORO_TTS_URL", "http://localhost:8880")
BASE_URL = os.getenv("BASE_URL", "https://omi.apps.hilo.ca")

# Audio storage (in-memory, clears on restart)
audio_cache: dict[str, dict] = {}
AUDIO_EXPIRY_MINUTES = 30

# Conversation history storage
conversation_history: list[dict] = []
MAX_HISTORY = 100


def cleanup_old_audio():
    """Remove audio older than expiry time."""
    now = datetime.now()
    expired = [k for k, v in audio_cache.items()
               if now - v["created"] > timedelta(minutes=AUDIO_EXPIRY_MINUTES)]
    for k in expired:
        del audio_cache[k]


def extract_portuguese_phrase(suggestion: str) -> str | None:
    """Extract the Portuguese follow-up phrase from the AI suggestion."""
    # Look for patterns like:
    # 💬 Say: "O que você mais sente falta dela?"
    # The Portuguese phrase is in quotes after "Say:"

    patterns = [
        r'Say:\s*"([^"]+)"',   # Primary format: Say: "..."
        r'💬\s*Say:\s*"([^"]+)"',
        r'💬[^"]*"([^"]+)"',   # Fallback: 💬 followed by quoted text
        r'Ask:\s*"([^"]+)"',
        r'Try:\s*"([^"]+)"',
    ]

    for pattern in patterns:
        match = re.search(pattern, suggestion)
        if match:
            phrase = match.group(1)
            # Check if it's Portuguese (not the English translation in parentheses)
            # Portuguese phrases typically have these markers
            portuguese_markers = ['você', 'como', 'que', 'isso', 'muito', 'para', 'mais',
                                  'está', 'isso', 'fazer', 'pode', 'seu', 'sua', 'ter',
                                  'ser', 'uma', 'não', 'sim', 'bem']
            has_accents = any(c in phrase for c in 'áàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ')
            has_portuguese_words = any(w in phrase.lower() for w in portuguese_markers)

            if has_accents or has_portuguese_words:
                return phrase

    return None


async def generate_tts(text: str, voice: str = "pf_dora") -> bytes | None:
    """
    Generate speech audio from text using Kokoro TTS.

    Voices for Brazilian Portuguese (p = Portuguese):
    - pf_dora (female) - recommended
    - pm_alex (male)
    - pm_santa (male)

    Voice naming: [lang][gender]_[name]
    p = Portuguese, b = British, a = American, f = female, m = male
    """
    try:
        async with httpx.AsyncClient(timeout=30.0) as http_client:
            response = await http_client.post(
                f"{KOKORO_TTS_URL}/v1/audio/speech",
                json={
                    "model": "kokoro",
                    "input": text,
                    "voice": voice,
                    "response_format": "mp3"
                }
            )
            if response.status_code == 200:
                return response.content
            else:
                print(f"TTS error: {response.status_code} - {response.text}")
                return None
    except Exception as e:
        print(f"TTS connection error: {e}")
        return None

# Store recent context for better suggestions
conversation_context = []


class TranscriptSegment(BaseModel):
    """Incoming transcript segment from Omi."""
    text: str
    speaker: Optional[str] = None
    speaker_id: Optional[int] = None
    is_user: Optional[bool] = False
    timestamp: Optional[float] = None


class WebhookPayload(BaseModel):
    """Full webhook payload from Omi."""
    session_id: Optional[str] = None
    segments: list[TranscriptSegment] = []


@app.get("/")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok", "app": "Bilingual Conversation Coach"}


@app.post("/webhook")
async def handle_transcript(request: Request):
    """
    Main webhook endpoint for Omi real-time transcripts.

    Omi sends transcript segments as they happen.
    We analyze and return translation + suggested follow-up.
    """
    try:
        data = await request.json()
        print(f"Received: {data}")

        # Extract transcript text
        # Omi may send different payload formats - handle flexibly
        if isinstance(data, dict):
            # Try common payload structures
            transcript = data.get("transcript", "")
            if not transcript:
                segments = data.get("segments", [])
                if segments:
                    # Get the most recent non-user segment
                    for seg in reversed(segments):
                        if isinstance(seg, dict) and not seg.get("is_user", False):
                            transcript = seg.get("text", "")
                            break
            if not transcript:
                transcript = data.get("text", "")
        else:
            transcript = str(data)

        if not transcript or len(transcript.strip()) < 3:
            return JSONResponse({"message": None})

        # Add to context (keep last 5 exchanges)
        conversation_context.append(transcript)
        if len(conversation_context) > 5:
            conversation_context.pop(0)

        # Get AI coaching response
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Fast and cheap for real-time
            messages=[
                {"role": "system", "content": REALTIME_SYSTEM_PROMPT},
                {"role": "user", "content": f"Recent context: {' | '.join(conversation_context[-3:])}\n\nLatest: {transcript}"}
            ],
            max_tokens=150,
            temperature=0.7
        )

        suggestion = response.choices[0].message.content.strip()

        # Skip if no action needed
        if "No action needed" in suggestion or suggestion == "":
            return JSONResponse({"message": None})

        print(f"Suggestion: {suggestion}")

        # Generate TTS for the Portuguese phrase
        portuguese_phrase = extract_portuguese_phrase(suggestion)
        audio_url = None

        if portuguese_phrase:
            print(f"Generating audio for: {portuguese_phrase}")
            audio_data = await generate_tts(portuguese_phrase)

            if audio_data:
                # Store audio with unique ID
                audio_id = str(uuid.uuid4())[:8]
                audio_cache[audio_id] = {
                    "audio": audio_data,
                    "phrase": portuguese_phrase,
                    "created": datetime.now()
                }
                audio_url = f"{BASE_URL}/audio/{audio_id}"
                print(f"Audio stored: {audio_url}")

                # Cleanup old audio periodically
                cleanup_old_audio()

        # Build response message - keep it short, Omi may truncate
        message = suggestion
        if audio_url:
            # Short format to avoid truncation
            short_id = audio_url.split("/")[-1]
            message += f"\n🔊 omi.apps.hilo.ca/audio/{short_id}"

        print(f"=== FULL RESPONSE ===")
        print(f"{message}")
        print(f"=====================")

        # Store in conversation history
        conversation_history.append({
            "id": str(uuid.uuid4())[:8],
            "timestamp": datetime.now().isoformat(),
            "original": transcript,
            "suggestion": suggestion,
            "portuguese_phrase": portuguese_phrase,
            "audio_url": audio_url,
        })

        # Keep history bounded
        while len(conversation_history) > MAX_HISTORY:
            conversation_history.pop(0)

        return JSONResponse({
            "message": message,
            "notify": True
        })

    except Exception as e:
        print(f"Error: {e}")
        return JSONResponse({"message": None, "error": str(e)})


@app.post("/translate")
async def translate_only(request: Request):
    """Simple translation endpoint for testing."""
    data = await request.json()
    text = data.get("text", "")

    if not text:
        raise HTTPException(status_code=400, detail="No text provided")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Translate between English and Brazilian Portuguese. Be natural, not literal. Just return the translation."},
            {"role": "user", "content": text}
        ],
        max_tokens=100
    )

    return {"translation": response.choices[0].message.content.strip()}


@app.post("/memory-created")
async def handle_memory_created(request: Request):
    """
    Webhook for when a memory is created (conversation ends).
    Can be used to send a full conversation summary.
    """
    data = await request.json()
    print(f"Memory created: {data}")

    # Clear conversation context for next conversation
    conversation_context.clear()

    return JSONResponse({"status": "received"})


@app.post("/tts")
async def text_to_speech(request: Request):
    """
    Generate Brazilian Portuguese audio for a phrase.

    POST /tts
    {"text": "Como você está?", "voice": "bf_isabella"}

    Returns: MP3 audio
    """
    data = await request.json()
    text = data.get("text", "")
    voice = data.get("voice", "pf_dora")  # Default to Brazilian Portuguese female

    if not text:
        raise HTTPException(status_code=400, detail="No text provided")

    print(f"Generating TTS for: {text}")
    audio = await generate_tts(text, voice)

    if audio:
        return Response(content=audio, media_type="audio/mpeg")
    else:
        raise HTTPException(status_code=503, detail="TTS service unavailable")


@app.get("/tts/test")
async def test_tts():
    """Test TTS with a sample phrase."""
    test_phrase = "Olá, como você está hoje?"
    audio = await generate_tts(test_phrase)

    if audio:
        return Response(content=audio, media_type="audio/mpeg")
    else:
        return JSONResponse({
            "error": "TTS unavailable",
            "kokoro_url": KOKORO_TTS_URL,
            "hint": "Set KOKORO_TTS_URL env variable to your Kokoro endpoint"
        }, status_code=503)


@app.get("/audio/{audio_id}")
async def get_audio(audio_id: str):
    """
    Serve stored audio by ID.

    Example: GET /audio/abc123
    Returns: MP3 audio file
    """
    if audio_id not in audio_cache:
        raise HTTPException(status_code=404, detail="Audio not found or expired")

    audio_data = audio_cache[audio_id]
    return Response(
        content=audio_data["audio"],
        media_type="audio/mpeg",
        headers={
            "Content-Disposition": f'inline; filename="phrase-{audio_id}.mp3"'
        }
    )


@app.get("/audio/{audio_id}/info")
async def get_audio_info(audio_id: str):
    """Get info about stored audio."""
    if audio_id not in audio_cache:
        raise HTTPException(status_code=404, detail="Audio not found or expired")

    audio_data = audio_cache[audio_id]
    return {
        "id": audio_id,
        "phrase": audio_data["phrase"],
        "created": audio_data["created"].isoformat(),
        "url": f"{BASE_URL}/audio/{audio_id}"
    }


# ============== UI ==============

@app.get("/api/conversations")
async def get_conversations():
    """Get conversation history."""
    return {"conversations": list(reversed(conversation_history))}


@app.get("/ui", response_class=HTMLResponse)
async def dashboard():
    """Simple dashboard UI showing conversations and audio."""
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bilingual Coach - Dashboard</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            color: #fff;
            padding: 20px;
        }
        .container { max-width: 800px; margin: 0 auto; }
        h1 {
            text-align: center;
            margin-bottom: 10px;
            font-size: 2em;
        }
        .subtitle {
            text-align: center;
            color: #888;
            margin-bottom: 30px;
        }
        .stats {
            display: flex;
            gap: 20px;
            justify-content: center;
            margin-bottom: 30px;
        }
        .stat {
            background: rgba(255,255,255,0.1);
            padding: 15px 25px;
            border-radius: 10px;
            text-align: center;
        }
        .stat-value { font-size: 2em; font-weight: bold; color: #4ade80; }
        .stat-label { color: #888; font-size: 0.9em; }
        .conversation {
            background: rgba(255,255,255,0.05);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
            border-left: 4px solid #4ade80;
        }
        .conversation:hover { background: rgba(255,255,255,0.08); }
        .time {
            color: #666;
            font-size: 0.8em;
            margin-bottom: 10px;
        }
        .original {
            color: #fbbf24;
            font-size: 1.1em;
            margin-bottom: 10px;
        }
        .original::before { content: '🇧🇷 '; }
        .translation {
            color: #94a3b8;
            margin-bottom: 10px;
            padding-left: 20px;
            border-left: 2px solid #333;
        }
        .suggestion {
            background: rgba(74, 222, 128, 0.1);
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 10px;
        }
        .portuguese-phrase {
            color: #4ade80;
            font-size: 1.1em;
            font-weight: 500;
        }
        .audio-player {
            margin-top: 10px;
        }
        audio {
            width: 100%;
            height: 40px;
            border-radius: 20px;
        }
        .no-audio {
            color: #666;
            font-style: italic;
            font-size: 0.9em;
        }
        .empty {
            text-align: center;
            padding: 60px;
            color: #666;
        }
        .refresh-btn {
            display: block;
            margin: 0 auto 30px;
            padding: 10px 30px;
            background: #4ade80;
            color: #000;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
        }
        .refresh-btn:hover { background: #22c55e; }
        .live-indicator {
            display: inline-block;
            width: 10px;
            height: 10px;
            background: #4ade80;
            border-radius: 50%;
            margin-right: 8px;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        .controls {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        .toggle-btn {
            padding: 10px 20px;
            background: rgba(255,255,255,0.1);
            color: #fff;
            border: 2px solid #4ade80;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s;
        }
        .toggle-btn.active {
            background: #4ade80;
            color: #000;
        }
        .toggle-btn:hover { opacity: 0.8; }
        .new-audio {
            animation: glow 1s ease-in-out;
        }
        @keyframes glow {
            0%, 100% { box-shadow: 0 0 0 rgba(74, 222, 128, 0); }
            50% { box-shadow: 0 0 30px rgba(74, 222, 128, 0.8); }
        }
        .now-playing {
            background: rgba(74, 222, 128, 0.2);
            border-left-color: #fbbf24;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🗣️ Bilingual Coach</h1>
        <p class="subtitle">English ↔ Brazilian Portuguese</p>

        <div class="stats">
            <div class="stat">
                <div class="stat-value" id="total-count">-</div>
                <div class="stat-label">Conversations</div>
            </div>
            <div class="stat">
                <div class="stat-value" id="audio-count">-</div>
                <div class="stat-label">Audio Generated</div>
            </div>
        </div>

        <div class="controls">
            <button class="toggle-btn active" id="autoplay-btn" onclick="toggleAutoplay()">
                🔊 Auto-Play ON
            </button>
            <button class="refresh-btn" onclick="loadConversations()">
                <span class="live-indicator"></span> Refresh
            </button>
        </div>

        <div id="conversations"></div>
    </div>

    <script>
        let autoplayEnabled = true;
        let lastSeenId = null;
        let currentAudio = null;

        function toggleAutoplay() {
            autoplayEnabled = !autoplayEnabled;
            const btn = document.getElementById('autoplay-btn');
            btn.textContent = autoplayEnabled ? '🔊 Auto-Play ON' : '🔇 Auto-Play OFF';
            btn.classList.toggle('active', autoplayEnabled);
        }

        async function loadConversations() {
            try {
                const res = await fetch('/api/conversations');
                const data = await res.json();

                document.getElementById('total-count').textContent = data.conversations.length;
                document.getElementById('audio-count').textContent =
                    data.conversations.filter(c => c.audio_url).length;

                const container = document.getElementById('conversations');

                if (data.conversations.length === 0) {
                    container.innerHTML = '<div class="empty">No conversations yet.<br>Start speaking Portuguese with Omi!</div>';
                    return;
                }

                // Check for new conversation with audio
                const newest = data.conversations[0];
                if (newest && newest.id !== lastSeenId && newest.audio_url && autoplayEnabled) {
                    // New conversation with audio - will auto-play after render
                    setTimeout(() => playNewestAudio(newest.id), 100);
                }
                lastSeenId = newest?.id;

                container.innerHTML = data.conversations.map((conv, idx) => `
                    <div class="conversation" id="conv-${conv.id}" ${idx === 0 ? 'data-newest="true"' : ''}>
                        <div class="time">${new Date(conv.timestamp).toLocaleString()}</div>
                        <div class="original">${escapeHtml(conv.original)}</div>
                        <div class="suggestion">${formatSuggestion(conv.suggestion)}</div>
                        ${conv.portuguese_phrase ? `
                            <div class="portuguese-phrase">💬 "${escapeHtml(conv.portuguese_phrase)}"</div>
                        ` : ''}
                        ${conv.audio_url ? `
                            <div class="audio-player">
                                <audio id="audio-${conv.id}" controls src="${conv.audio_url}"
                                    onplay="onAudioPlay('${conv.id}')" onended="onAudioEnd('${conv.id}')"></audio>
                            </div>
                        ` : '<div class="no-audio">No audio generated</div>'}
                    </div>
                `).join('');
            } catch (err) {
                console.error('Failed to load:', err);
            }
        }

        function playNewestAudio(id) {
            const audio = document.getElementById('audio-' + id);
            if (audio) {
                // Stop any currently playing audio
                if (currentAudio && currentAudio !== audio) {
                    currentAudio.pause();
                }
                audio.play().catch(e => console.log('Autoplay blocked:', e));
                currentAudio = audio;

                // Highlight the conversation
                const conv = document.getElementById('conv-' + id);
                if (conv) {
                    conv.classList.add('new-audio');
                }
            }
        }

        function onAudioPlay(id) {
            const conv = document.getElementById('conv-' + id);
            if (conv) conv.classList.add('now-playing');
        }

        function onAudioEnd(id) {
            const conv = document.getElementById('conv-' + id);
            if (conv) conv.classList.remove('now-playing');
        }

        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }

        function formatSuggestion(text) {
            return escapeHtml(text)
                .replace(/🔄/g, '<br>🔄')
                .replace(/💬/g, '<br>💬')
                .replace(/🇧🇷/g, '<br>🇧🇷');
        }

        // Load on start
        loadConversations();

        // Auto-refresh every 3 seconds for real-time feel
        setInterval(loadConversations, 3000);
    </script>
</body>
</html>
    """
    return HTMLResponse(content=html)


if __name__ == "__main__":
    import uvicorn

    if not os.getenv("OPENAI_API_KEY"):
        print("Warning: OPENAI_API_KEY not set!")
        print("Set it with: set OPENAI_API_KEY=your-key-here")

    print("\n🚀 Starting Bilingual Conversation Coach...")
    print("📡 Webhook URL: http://localhost:8000/webhook")
    print("🔗 Use ngrok to expose: ngrok http 8000\n")

    port = int(os.getenv("PORT", 3000))
    uvicorn.run(app, host="0.0.0.0", port=port)
