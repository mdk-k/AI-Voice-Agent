import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_API_BASE")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-mini")


def generate_response(conversation_history):
    """
    Generate a response using Azure OpenAI's ChatCompletion API, ensuring that the assistant only
    answers questions related to Jivus AI.
    """
    messages = [{
        "role": "system",
        "content": (
            "You are a professional sales agent for Jivus AI, an AI-powered search and conversational platform. "
            "You only answer questions related to Jivus AI, including its products, features, pricing, and integrations. "
            "If a question is outside of this scope, reply: 'I'm sorry, I only provide information about Jivus AI.'"
        )
    }]

    for turn in conversation_history:
        if turn.get("speaker", "").lower() == "customer":
            messages.append({"role": "user", "content": turn.get("text", "")})
        elif turn.get("speaker", "").lower() == "agent":
            messages.append({"role": "assistant", "content": turn.get("text", "")})

    try:
        response = openai.ChatCompletion.create(
            engine=deployment_name,
            messages=messages,
            temperature=1,
            max_tokens=300
        )
        output_text = response.choices[0].message.content.strip()
        print("Azure ChatGPT API response:", output_text)
        return output_text
    except Exception as e:
        print("Error calling Azure OpenAI API:", e)
        return "I'm sorry, I couldn't generate a response at this time."


def main():
    conversation_history = []

    print("Enter your messages. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        conversation_history.append({"speaker": "customer", "text": user_input})
        agent_response = generate_response(conversation_history)
        conversation_history.append({"speaker": "agent", "text": agent_response})


if __name__ == "__main__":
    main()
