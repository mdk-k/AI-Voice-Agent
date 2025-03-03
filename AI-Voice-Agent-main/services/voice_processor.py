from datetime import datetime
from services.gpt_mini import generate_response
from services.elevenlabs import synthesize_speech
from services.logger import log_conversation

# Global session dictionary to track metadata and conversation history.
conversation_session = {
    "metadata": {},
    "conversation_history": []
}

def process_initial_call(call_sid, caller_number, called_number):
    """
    Initializes the conversation session with metadata.
    """
    global conversation_session
    conversation_session["metadata"] = {
        "call_sid": call_sid,
        "caller_number": caller_number,
        "called_number": called_number,
        "start_time": datetime.now().isoformat(),
    }
    conversation_session["conversation_history"].clear()

def process_gathered_input(caller_text, timestamp):
    """
    Processes the caller's speech input, generates an AI response, and logs the conversation.
    """
    global conversation_session

    # Ensure metadata exists before processing input
    if "start_time" not in conversation_session["metadata"]:
        process_initial_call("UNKNOWN_SID", "UNKNOWN_CALLER", "UNKNOWN_RECEIVER")

    # Append customer input to conversation history
    conversation_session["conversation_history"].append({
        'speaker': 'customer',
        'text': caller_text,
        'timestamp': timestamp.isoformat()
    })

    # Generate AI response using the full conversation history
    ai_response = generate_response(conversation_session["conversation_history"])

    # Append AI response to conversation history
    conversation_session["conversation_history"].append({
        'speaker': 'agent',
        'text': ai_response,
        'timestamp': datetime.now().isoformat()
    })

    # Synthesize speech from the AI response (saved as static/agent_response.mp3)
    synthesize_speech(ai_response)

    # Log the conversation with metadata
    log_conversation(conversation_session)
