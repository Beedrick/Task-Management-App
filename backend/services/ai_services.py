from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Please add your OpenAI API key to a .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def auto_prioritize_tasks(tasks):
    
    prompt = "You are an intelligent and clever assistant that prioritizes tasks based on urgency, deadlines, and importance"

    for task in tasks:
        prompt += f"- Task: {task.title}\n"
        if task.description:
            prompt += f"  Description: {task.description}\n"
        if task.deadline:
            prompt += f"  Deadline: {task.deadline}\n"
        prompt += f"  Urgency: {task.urgency}\n"
        prompt += f"  Category: {task.category}\n"
        prompt += f"  Importance Level: {task.importance}/10\n\n"

    prompt += "Return the tasks in order of priority with reasoning. Ensure that you consider all urgencies, deadlines and importances before making your prioritization final. Also, carefully anzlyze the descriptions of each task and its deadlines and make judgments on if they could have possible dependencies."

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role":"user", "content": prompt}]
    )

    return response.choices[0].message
