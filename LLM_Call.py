from dotenv import load_dotenv
from groq import Groq
import os


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What should my next workout be if I exercised my biceps yesterday?",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)
