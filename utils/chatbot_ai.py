import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_fitness_ai(question):

    prompt = f"""
You are  VitaCore  AI, an AI fitness assistant.

Answer the user's question in a professional, easy-to-understand way.

Rules:
- Answer in approximately 250–300 words.
- Do NOT use Markdown symbols like **, ##, ---, or *.
- Use plain text only.
- Keep the explanation informative but not too long.
- Divide the answer into clear sections.
- Write section headings in UPPERCASE.
- Leave one blank line between sections.
- Give practical advice whenever possible.


 VitaCore  AI TIP

BMI is a useful screening tool, but it does not distinguish muscle from body fat. People with high muscle mass may have a higher BMI while still being healthy. Consider body fat percentage, waist circumference, and overall fitness along with BMI.

Question:
{question}
"""

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"