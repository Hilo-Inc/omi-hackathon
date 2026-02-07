"""
Bilingual Conversation Coach - Real-time Webhook Server
Receives live transcripts from Omi and returns translations + follow-up suggestions.
"""

import os
import httpx
import base64
import re
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel
from typing import Optional
import openai
from prompts import REALTIME_SYSTEM_PROMPT

# Initialize
app = FastAPI(title="Bilingual Conversation Coach")
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# TTS Configuration
KOKORO_TTS_URL = os.getenv("KOKORO_TTS_URL", "http://localhost:8880")


async def generate_tts(text: str, voice: str = "bf_isabella") -> bytes | None:
    """
    Generate speech audio from text using Kokoro TTS.

    Voices for Brazilian Portuguese:
    - bf_isabella (female)
    - bm_lucas (male)
    - bf_camila (female)
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

        return JSONResponse({
            "message": suggestion,
            "notify": True  # Show as notification
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
    voice = data.get("voice", "bf_isabella")  # Default to female Brazilian voice

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
