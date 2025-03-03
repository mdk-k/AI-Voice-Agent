# AI Voice Agent
AI Voice Agent is an AI-powered sales representative that handles multi-turn conversations over phone calls. The agent integrates multiple cutting-edge technologies:

Vocode – for advanced voice interactions.
Twilio – for telephony integration (handling inbound/outbound calls).
OpenAI GPT-4o Mini – for dialogue generation (fine-tuned on sales and AI data).
Deepgram – for real-time speech-to-text transcription.
ElevenLabs – for text-to-speech (TTS) synthesis.
Conversation Logging – captures complete conversation history (with timestamps and call metadata).
Dashboard (Streamlit) – a simple UI to monitor live conversation logs.
The system is designed to maintain context throughout the conversation, provide sales-oriented responses, and optimize response times for real-time engagement.

## Table of Contents
Features
Architecture
Prerequisites
Setup & Installation
Environment Variables
Running the Project
Using Ngrok for Public Exposure
Fine-Tuning & Deployment
Dashboard
License

### Features
Call Handling:
Receive and process incoming calls via Twilio.

Speech-to-Text:
Transcribe customer speech using Deepgram with minimal latency.

Conversational AI:
Generate sales-oriented, context-aware responses using a fine-tuned GPT-4o Mini model deployed on Azure OpenAI.

Text-to-Speech:
Convert AI-generated responses to natural-sounding audio using ElevenLabs TTS.

Conversation Logging:
Log conversation details (customer input, AI responses, timestamps, call metadata) in a structured format (JSON).

Live Monitoring Dashboard:
A simple Streamlit dashboard to view live conversation logs.

Real-time Engagement Optimization:
Techniques such as asynchronous processing, caching, and efficient context management ensure fast responses.

#### Architecture
Call Handling (Twilio):

Incoming calls are received by Twilio.
A webhook endpoint (implemented in Flask) processes the call.
The <Gather> verb is used to capture customer speech.
Speech-to-Text (Deepgram):

Customer speech is transcribed into text using Deepgram's API.
Conversational AI (Azure OpenAI GPT-4o Mini):

Transcribed text and conversation history are passed to the fine-tuned GPT-4o Mini model for generating responses.
The model is fine-tuned on sales data to focus solely on AI–related queries.
Text-to-Speech (ElevenLabs):

The AI response is converted to audio using ElevenLabs TTS and saved as an MP3 file accessible via a public URL.
Conversation Logging:

Conversation details (including timestamps and call metadata) are logged to JSON files.
Dashboard (Streamlit):

A simple web UI displays live conversation logs for monitoring.
