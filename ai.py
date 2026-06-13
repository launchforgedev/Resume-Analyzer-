import json
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def analyze_resume(resume_text, user_goal):

    prompt = f"""
    You are a career advisor.

    Resume:
    {resume_text}

    User Goal:
    {user_goal}

    Return only JSON:
    {{
        "skills": [],
        "missing_skills": [],
        "roadmap": [],
        "interview_questions": []
    }}
    """

    try:

        client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        content = response.text.strip()

        start = content.find("{")
        end = content.rfind("}") + 1

        return json.loads(content[start:end])

    except Exception as e:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": str(e)
        }