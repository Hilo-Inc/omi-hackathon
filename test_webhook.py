"""
Quick test script to verify the webhook works locally.
Run the server first: python webhook/server.py
Then run this: python test_webhook.py
"""

import requests

BASE_URL = "http://localhost:8000"

# Test cases
test_segments = [
    # Portuguese that needs translation
    {"text": "Ah, foi muito difícil quando minha mãe ficou doente, sabe?"},
    {"text": "A gente sempre dá um jeito, né? Faz parte da vida."},
    {"text": "Tenho muita saudade daquela época."},

    # English (should skip or minimal response)
    {"text": "Yeah, I've been working at that company for a while."},

    # Mixed/emotional moments
    {"text": "Ela era tudo pra mim, minha melhor amiga."},
]

print("🧪 Testing Bilingual Conversation Coach Webhook\n")
print("=" * 50)

for i, segment in enumerate(test_segments, 1):
    print(f"\n📝 Test {i}: \"{segment['text'][:50]}...\"")
    try:
        response = requests.post(
            f"{BASE_URL}/webhook",
            json={"transcript": segment["text"]}
        )
        result = response.json()
        if result.get("message"):
            print(f"✅ Response:\n{result['message']}")
        else:
            print("⏭️  Skipped (no translation needed)")
    except requests.exceptions.ConnectionError:
        print("❌ Error: Server not running! Start with: python webhook/server.py")
        break
    except Exception as e:
        print(f"❌ Error: {e}")

print("\n" + "=" * 50)
print("🎯 Test the /translate endpoint:")
try:
    response = requests.post(
        f"{BASE_URL}/translate",
        json={"text": "Estou com saudade de casa"}
    )
    print(f"   Input: 'Estou com saudade de casa'")
    print(f"   Output: {response.json().get('translation')}")
except:
    print("   (Server not running)")
