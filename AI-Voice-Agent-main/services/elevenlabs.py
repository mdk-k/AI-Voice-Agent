# services/elevenlabs.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
ELEVENLABS_TTS_URL = os.getenv('ELEVENLABS_TTS_URL')

def synthesize_speech(text):
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.75,         # Adjust these values as needed
            "similarity_boost": 0.75
        }
    }
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    response = requests.post(ELEVENLABS_TTS_URL, json=payload, headers=headers, stream=True)
    response.raise_for_status()
    audio_data = response.content
    # Save the audio to the static folder for public access.
    with open("static/agent_response.mp3", "wb") as f:
        f.write(audio_data)
    print("Synthesized speech saved as static/agent_response.mp3")
    return audio_data
