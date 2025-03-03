# services/deepgram.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

DEEPGRAM_API_KEY = os.getenv('DEEPGRAM_API_KEY')
DEEPGRAM_API_URL = 'https://api.deepgram.com/v1/listen'

def transcribe_audio(audio_file_path):
    headers = {
        'Authorization': f'Token {DEEPGRAM_API_KEY}'
    }
    with open(audio_file_path, 'rb') as audio_file:
        response = requests.post(DEEPGRAM_API_URL, headers=headers, data=audio_file)
    response.raise_for_status()
    result = response.json()
    transcript = result['results']['channels'][0]['alternatives'][0]['transcript']
    print("Transcription result:", transcript)
    return transcript
