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
.Architecture
.Prerequisites
.Setup & Installation
.Environment Variables
.Running the Project
.Using Ngrok for Public Exposure


### Features
**Call Handling**:
  Receive and process incoming calls via Twilio.

.**Speech-to-Text**:
  Transcribe customer speech using Deepgram with minimal latency.

.**Conversational AI**:
  Generate sales-oriented, context-aware responses using a fine-tuned GPT-4o Mini model deployed on Azure OpenAI.

.**Text-to-Speech**:
  Convert AI-generated responses to natural-sounding audio using ElevenLabs TTS.

.**Conversation Logging**:
  Log conversation details (customer input, AI responses, timestamps, call metadata) in a structured format (JSON).

.**Live Monitoring Dashboard**:
  A simple Streamlit dashboard to view live conversation logs.

.**Real-time Engagement Optimization**:
  Techniques such as asynchronous processing, caching, and efficient context management ensure fast responses.

#### Architecture
   1. **Call Handling (Twilio)**:
       Incoming calls are received by Twilio.
       A webhook endpoint (implemented in Flask) processes the call.
       The <Gather> verb is used to capture customer speech.
      
   2.  **Speech-to-Text (Deepgram)**:
       Customer speech is transcribed into text using Deepgram's API.
       
   3. **Conversational AI (Azure OpenAI GPT-4o Mini)**:
       Transcribed text and conversation history are passed to the fine-tuned GPT-4o Mini model for generating responses.
       The model is fine-tuned on sales data to focus solely on AI–related queries.
      
   4. **Text-to-Speech (ElevenLabs)**:
        The AI response is converted to audio using ElevenLabs TTS and saved as an MP3 file accessible via a public URL.
      
   5.   **Conversation Logging**:
        Conversation details (including timestamps and call metadata) are logged to JSON files.
        
   6.  **Dashboard (Streamlit)**:
        A simple web UI displays live conversation logs for monitoring.

##### Prerequisites
.**Python 3.8+**
.**Twilio Account** with a purchased phone number
.**Deepgram API Key**
.**ElevenLabs API Key and TTS Endpoint**
.**Azure OpenAI Resource** (with fine-tuning access for GPT-4o Mini)
.**Required Python Libraries**:
   Flask
   OpenAI
   Requests
   python-dotenv
   Streamlit (for dashboard)
   streamlit-autorefresh (optional)

  ###### Setup & Installation
1. **Clone the Repository**:

    git clone https://github.com/yourusername/ ai-voice-agent.git
    cd ai-voice-agent
2. **Create and Activate a Virtual Environment**:

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install Dependencies**:

    pip install -r requirements.txt
    Sample requirements.txt:

       Flask
       openai
       requests
       python-dotenv
       streamlit
       streamlit-autorefresh

  ###### Environment Variables
  Create a .env file in the root directory with the following contents (replace placeholder values):

# Twilio 
TWILIO_ACCOUNT_SID=YOUR_TWILIO_ACCOUNT_SID
TWILIO_AUTH_TOKEN=YOUR_TWILIO_AUTH_TOKEN

# Deepgram
DEEPGRAM_API_KEY=YOUR_DEEPGRAM_API_KEY

# Azure OpenAI
AZURE_OPENAI_API_KEY=KEY_HERE
AZURE_OPENAI_API_BASE=https:// a.openai.azure.com
AZURE_OPENAI_API_VERSION=2025-01-01-preview
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o-mini-2024-07-18-ft-c34a629ff3044217a959c83035583e41

# ElevenLabs
ELEVENLABS_API_KEY=YOUR_ELEVENLABS_API_KEY
ELEVENLABS_TTS_URL=https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM/stream
ELEVENLABS_VOICE=default_voice
Important: Do not expose your API keys publicly.

**Running the Project**
1. Running the Flask Application (Twilio Webhooks & AI Processing)
Run the Flask server:

python app.py
Ensure your server is publicly accessible (e.g., via ngrok) and configure your Twilio phone number webhook to point to the appropriate URL (e.g., https://<your-ngrok-id>.ngrok-free.app/twilio/incoming).

2. Testing the Conversation Flow (Text-Based)
Use a test script (like test_gpt_mini.py) to simulate multi-turn conversation interactions:

python test_gpt_mini.py
3. Running the Dashboard (Streamlit)
To monitor live conversation logs:

streamlit run streamlit_dashboard.py
This dashboard displays logs from the logs/ folder and auto-refreshes to show the latest conversation data.

**Using Ngrok for Public Exposure**
When developing locally, you can use ngrok to expose your Flask server to the public internet. This is essential for testing Twilio webhooks.

Install ngrok:
Download and install ngrok from ngrok.com.

Start an ngrok Tunnel:
If your Flask app is running on port 5000, open a new terminal and run:

ngrok http 5000
ngrok will provide you with a public URL (e.g., https://<your-ngrok-id>.ngrok-free.app).

Configure Twilio:
Update your Twilio phone number webhook to point to:

https://<your-ngrok-id>.ngrok-free.app/twilio/incoming
Update Any Hardcoded URLs:
If your project code includes any hardcoded URLs (for example, in TTS playback), ensure they use your current ngrok URL.
