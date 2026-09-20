import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_diet_plan(user):

    prompt = f"""
Generate a simple one-day diet plan for the following user.

Name: {user.name}
Goal: {user.goal}

Rules:
- Do NOT use Markdown.
- Do NOT use ** or ## or ---.
- Do NOT use bullet symbols like *.
- Keep the response under 200 words.
- Return only plain text.

Format:

Breakfast:
...

Morning Snack:
...

Lunch:
...

Evening Snack:
...

Dinner:
...

Water Intake:
...

Fitness Tip:
...
"""

    try:

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt,
        )

        return response.text

    except Exception:

        return """
Unable to generate an AI diet plan.

Reason:
• Gemini API quota has been exceeded
• OR there is a temporary connection issue

Please try again later.
"""