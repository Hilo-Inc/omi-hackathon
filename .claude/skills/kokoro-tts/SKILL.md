---
name: kokoro-tts
description: Generate high-quality text-to-speech audio using Kokoro TTS. Use when the user says "generate audio", "text to speech", "TTS", "narration", "voice over", "read aloud", "create audio", or wants to convert text to speech.
allowed-tools:
  - Read
  - Bash
  - Write
  - Glob
---

# Kokoro TTS - Text-to-Speech Generator

Generate high-quality text-to-speech audio using the Kokoro-FastAPI local TTS engine.

## Prerequisites

- Kokoro-FastAPI Docker container running on `http://localhost:8880`
- ffprobe (optional, for duration reporting)

## Quick Start

```bash
# Check if Kokoro is running
curl -s http://localhost:8880/v1/audio/voices

# Generate speech
curl -s -X POST http://localhost:8880/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{"model": "kokoro", "input": "Your text here", "voice": "af_heart", "speed": 1.0, "response_format": "mp3"}' \
  --output output.mp3
```

## Arguments

The skill accepts: `$ARGUMENTS`

Parse arguments for:
- **Text source**: Direct text, file path, or markdown file reference
- **Voice**: Voice ID (default: `af_heart`)
- **Speed**: Playback speed 0.5-2.0 (default: `1.0`)
- **Output**: Output file path (default: `./output.mp3`)
- **Format**: mp3, wav, opus, flac (default: `mp3`)

Example invocations:
- `/kokoro-tts "Hello world"` - Generate with defaults
- `/kokoro-tts @script.md --voice am_adam` - Read from file with male voice
- `/kokoro-tts "Welcome" --output welcome.mp3 --speed 0.9` - Custom output and speed

## Workflow

### Step 1: Verify Kokoro is Running

```bash
curl -s http://localhost:8880/v1/audio/voices
```

If not running, inform the user:
> Kokoro TTS is not available. Please start the Docker container:
> ```
> docker run -p 8880:8880 ghcr.io/remsky/kokoro-fastapi:latest
> ```

### Step 2: Parse Input

1. **Direct text**: Use the provided text directly
2. **File reference** (`@filename`): Read the file content
3. **Markdown file**: Extract text, removing markdown formatting and stage directions like `[pause]`, `*emphasis*`

For presentation scripts, split by slide markers (`## [SLIDE`) and generate individual files.

### Step 3: Generate Audio

```bash
curl -s -X POST http://localhost:8880/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kokoro",
    "input": "<TEXT>",
    "voice": "<VOICE_ID>",
    "speed": <SPEED>,
    "response_format": "<FORMAT>"
  }' \
  --output "<OUTPUT_PATH>"
```

### Step 4: Report Results

After generation, report:
- File path
- Duration (if ffprobe available)
- Voice used
- Any errors encountered

## Available Voices

### American English
| Voice ID | Name | Gender |
|----------|------|--------|
| af_heart | Heart | Female |
| af_bella | Bella | Female |
| af_nicole | Nicole | Female |
| af_sarah | Sarah | Female |
| af_sky | Sky | Female |
| af_alloy | Alloy | Female |
| af_nova | Nova | Female |
| af_river | River | Female |
| am_adam | Adam | Male |
| am_michael | Michael | Male |
| am_eric | Eric | Male |
| am_fenrir | Fenrir | Male |
| am_liam | Liam | Male |

### British English
| Voice ID | Name | Gender |
|----------|------|--------|
| bf_alice | Alice | Female |
| bf_emma | Emma | Female |
| bf_lily | Lily | Female |
| bm_daniel | Daniel | Male |
| bm_george | George | Male |
| bm_lewis | Lewis | Male |

### Other Languages
| Voice ID | Language | Gender |
|----------|----------|--------|
| pf_dora | Portuguese (BR) | Female |
| pm_alex | Portuguese (BR) | Male |
| ff_siwis | French | Female |
| ef_dora | Spanish | Female |
| em_alex | Spanish | Male |
| jf_alpha | Japanese | Female |
| zf_xiaobei | Chinese | Female |
| zm_yunxi | Chinese | Male |

## Voice Recommendations

| Use Case | Recommended Voice |
|----------|-------------------|
| Professional presentation | af_heart, af_nicole |
| Narration/storytelling | af_bella, am_adam |
| Technical content | am_michael, bf_george |
| Friendly/casual | af_sky, af_nova |
| British accent | bf_emma, bm_george |

## Batch Processing

For multiple files (like presentation slides):

```bash
# Generate numbered slide narrations
for i in {1..30}; do
  text=$(extract_slide_text $i)
  curl -s -X POST http://localhost:8880/v1/audio/speech \
    -H "Content-Type: application/json" \
    -d "{\"model\": \"kokoro\", \"input\": \"$text\", \"voice\": \"af_heart\", \"speed\": 0.95, \"response_format\": \"mp3\"}" \
    --output "slide-$(printf '%02d' $i)-narration.mp3"
done
```

## Text Preprocessing

Before sending to TTS, clean the text:

1. Remove markdown formatting (`**bold**`, `*italic*`, `#` headers)
2. Remove stage directions (`[pause]`, `[smile]`, `[gesture]`)
3. Convert special characters to spoken form
4. Split long text into chunks (max ~500 words per request for best quality)

Example preprocessing:
```python
import re

def clean_for_tts(text):
    # Remove markdown
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)  # bold
    text = re.sub(r'\*(.+?)\*', r'\1', text)      # italic
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)  # headers

    # Remove stage directions
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\*\[.*?\]\*', '', text)

    return text.strip()
```

## Output Formats

| Format | Use Case | Quality |
|--------|----------|---------|
| mp3 | General use, web | Good compression |
| wav | Editing, processing | Lossless |
| opus | Streaming, low bandwidth | Excellent compression |
| flac | Archival | Lossless, compressed |

## Speed Settings

| Speed | Use Case |
|-------|----------|
| 0.8 | Very slow, for accessibility |
| 0.9 | Slow, for emphasis |
| 1.0 | Normal speed |
| 1.1 | Slightly faster |
| 1.2 | Fast, for summaries |

## Error Handling

| Error | Solution |
|-------|----------|
| Connection refused | Start Kokoro Docker container |
| Voice not found | Check available voices with `/v1/audio/voices` |
| Timeout | Split text into smaller chunks |
| Invalid format | Use mp3, wav, opus, or flac |

## Example: Generate Presentation Narration

```bash
# 1. Check Kokoro is running
curl -s http://localhost:8880/health

# 2. Generate individual slide narrations
curl -s -X POST http://localhost:8880/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kokoro",
    "input": "Good morning. Today we are going to talk about something important.",
    "voice": "af_heart",
    "speed": 0.95,
    "response_format": "mp3"
  }' \
  --output slide-01.mp3

# 3. Check duration
ffprobe -i slide-01.mp3 -show_entries format=duration -v quiet -of csv="p=0"
```

## Summary Template

After generating audio, provide a summary:

```markdown
## TTS Generation Complete

| File | Voice | Duration |
|------|-------|----------|
| output.mp3 | af_heart | 25.5s |

**Location:** `/path/to/output.mp3`
**Total Duration:** X seconds (X.X minutes)
```
