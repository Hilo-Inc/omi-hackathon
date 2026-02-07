# Bilingual Conversation Coach

An Omi app that helps you have deeper, more meaningful conversations across languages (English ↔ Brazilian Portuguese).

## Features

- **Part 1 (Memory Prompt)**: Post-conversation analysis with translations and cultural coaching
- **Part 2 (Real-time Webhook)**: Live translation + suggested follow-up questions

## Quick Start

### Part 1: Memory Prompt (No server needed)

1. Open Omi app → Explore → Create an App
2. Choose "Memory Prompt"
3. Paste the prompt from `prompts/memory-prompt.txt`
4. Test against an existing memory

### Part 2: Real-time Webhook

1. Install dependencies: `pip install -r requirements.txt`
2. Set your OpenAI API key: `set OPENAI_API_KEY=your-key`
3. Run locally: `python webhook/server.py`
4. Expose with ngrok: `ngrok http 8000`
5. Configure webhook URL in Omi Developer Mode

## Project Structure

```
omi-hackathon/
├── prompts/
│   ├── memory-prompt.txt      # Part 1: Post-conversation analysis
│   └── chat-prompt.txt        # Optional: Chat coaching persona
├── webhook/
│   ├── server.py              # Part 2: FastAPI webhook server
│   └── prompts.py             # System prompts for real-time
├── requirements.txt
└── README.md
```

## Demo Script (2 minutes)

1. Show a bilingual conversation memory
2. Run the memory prompt → show translated insights + cultural tips
3. (If Part 2 works) Show real-time translation appearing as you speak
