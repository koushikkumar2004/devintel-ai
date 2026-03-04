import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ask_ai(question: str):

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant for developers."
        },
        {
            "role": "user",
            "content": question
        }
    ],
    model="llama-3.1-8b-instant"
)

    return chat_completion.choices[0].message.content