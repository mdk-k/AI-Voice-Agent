import os
import json
import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

LOG_DIR = "logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    st.write("Logs directory created.")
else:
    st.write("Logs directory exists.")

st.title("Live Conversation Dashboard")
st.write("This dashboard displays the latest live conversation log from your AI voice agent.")

st_autorefresh(interval=1000, key="autorefresh_key")

log_files = sorted(
    [f for f in os.listdir(LOG_DIR) if f.endswith(".json")],
    key=lambda f: os.path.getmtime(os.path.join(LOG_DIR, f)),
    reverse=True
)

if log_files:
    latest_log_file = log_files[0]
    filepath = os.path.join(LOG_DIR, latest_log_file)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        st.subheader(f"Latest Conversation Log: {latest_log_file}")

        # Display metadata
        metadata = data.get("metadata", {})
        if metadata:
            st.markdown("**Metadata**")
            st.json(metadata)

        # Display conversation history (check both possible keys)
        conversation = data.get("conversation_history", data.get("conversation", []))
        if conversation:
            st.markdown("**Conversation History**")
            for message in conversation:
                speaker = message.get("speaker", "Unknown")
                text = message.get("text", "")
                timestamp = message.get("timestamp", "")
                st.markdown(f"**{speaker}:** {text}")
                st.caption(f"Timestamp: {timestamp}")
    except Exception as e:
        st.error(f"Error reading {latest_log_file}: {e}")
else:
    st.info("No conversation logs found.")

st.write(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
