from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def format_ai_response(response):
    content = response.choices[0].message.content
    tasks = content.split("\n\n")

    for idx, task in enumerate(tasks, start=1):
        print(f"Task {idx}:")
        lines = task.strip().split("\n")
        for line in lines:
            key, value = line.split(":", 1) if ":" in line else ("", line)
            key = key.strip()
            value = value.strip()

            if key:
                print(f"  {key}: {value}")
            else:
                print(f"  {value}")
        print("\n" + "-"*50 + "\n")

def auto_prioritize_tasks(tasks):
    prompt = """
You are an intelligent task management assistant. Your goal is to prioritize tasks logically and consistently based on urgency, deadlines, importance, and potential dependencies.
- **Deadline:** Tasks with the closest deadlines are generally prioritized higher.
- **Urgency:** Tasks marked as 'High' urgency are critical.
- **Importance:** Tasks rated higher on a scale of 1 to 10 are prioritized.
- **Dependencies:** Tasks that depend on other tasks must be done after their dependencies are completed.
- **Reasoning Requirement:** Provide structured reasoning for each prioritized task. Include deadline analysis, urgency assessment, importance ranking, and dependency checks.
- **Consistency:** Always ensure similar tasks are prioritized similarly in future requests.
- **Example of Ideal Output:**
  1. **Task:** Submit Report
     - **Reasoning:** Due in 3 hours, high importance (9/10), and no dependencies.
  2. **Task:** Prepare Presentation
     - **Reasoning:** Due tomorrow, medium urgency, but depends on gathering data first.
  3. **Task:** Buy Groceries
     - **Reasoning:** Due in 2 days, low urgency, and no dependencies.
"""

    for task in tasks:
        prompt += f"""
- **Task:** {task.title}
  - **Description:** {task.description if task.description else "No description provided"}
  - **Deadline:** {task.deadline}
  - **Urgency:** {task.urgency}
  - **Category:** {task.category}
  - **Importance:** {task.importance}/10
"""

    prompt += "\nPlease return the tasks in order of priority with detailed reasoning as shown in the example above."

    response = client.chat.completions.create(
        model="gpt-4",
        temperature=0.3,  
        messages=[{"role": "user", "content": prompt}]
    )

    format_ai_response(response)
    
    return response.choices[0].message.content
