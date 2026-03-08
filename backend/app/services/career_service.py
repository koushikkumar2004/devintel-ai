from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_career_advice(skills, interests, education):

    prompt = f"""
You are an AI career advisor.

Student details:
Skills: {skills}
Interests: {interests}
Education: {education}

Provide:
1. Recommended career paths
2. Skills they should learn next
3. Technologies they should focus on
4. Short explanation
"""

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama-3.1-8b-instant"
    )

    return chat_completion.choices[0].message.content