import os
import json
from datetime import datetime

LOG_DIR = "logs"

# Ensure the logs directory exists
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


def log_conversation(conversation_session):
    """
    Logs the full conversation including metadata, timestamps, and exchanges.
    """
    log_filename = os.path.join(LOG_DIR, f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")

    log_data = {
        "metadata": conversation_session["metadata"],
        "conversation": conversation_session["conversation_history"]
    }

    try:
        with open(log_filename, "w", encoding="utf-8") as log_file:
            json.dump(log_data, log_file, indent=4)
        print(f"✅ Conversation logged at {log_filename}")
    except Exception as e:
        print(f"❌ Error saving conversation log: {e}")
