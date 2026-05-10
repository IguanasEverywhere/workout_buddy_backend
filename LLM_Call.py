from dotenv import load_dotenv
from groq import Groq
import os


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

def call_groq(workouts_obj):

    context_str = 'My most recent workouts include: '

    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    for entry in workouts_obj.exercises:
        context_str += f'''
        {entry['exercise_name']} at {entry['weight']} lbs for {entry['reps']} reps.
        My notes from this exercise were: {entry['notes']}
        '''

    chat_completion = client.chat.completions.create(
        messages=[
            {
            "role": "system",
            "content": f"""
            Context:
            {context_str}
            """,
            },
            {
                "role": "user",
                "content": "Given my most recent workouts, what trends do you see, and what workout should I complete next? Refer to my most recent workouts in your answer."
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    # print(chat_completion.choices[0].message.content)
    workouts_obj.AI_feedback = chat_completion.choices[0].message.content
