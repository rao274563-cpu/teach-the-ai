import os
from click import prompt
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")
client = genai.Client(api_key=api_key)

REASONING_PROMPT = """
You are an Education reasoning evaluator.

The student is learning machine learning by teaching an AI student.

Current concept : OVERFITTING
The key idea the student should understand is:

A model can achieve very high accuracy on training data but still 
perform poorly on unseen data because it may have learned specific
to the training data instead of generalizable patterns.

Evaluate the student's explanation.

Return ONLY valid JSON with exactly these fields:

{
    "concept_understanding": 0-100,
    "reasoning_quality": 0-100,
    "generalization": 0-100,
    "misconception": "short description",
    "feedback": "short educational feedback"
}

Scoring guidance:

concept_understanding:
- Does the student understand the concept of overfitting?

reasoning_quality:
- Does the student explain why high training accuracy can be misleading?

generalization:
- Does the student understand performance on unseen data?

Important:
- Do not reward keyword matching alone.
- Evaluate the reasoning expressed by the student.
- Be fair to partially correct answers.
- Do not give a perfect score unless the explanation demonstrates
  genuine understanding.
- Keep feedback concise.

"""

def analyze_reasoning(student_answer: str) -> dict:
    """"
    Analyze the quality of student's explanation of overfitting.
    """

    prompt = f"""
{REASONING_PROMPT}

Student explanation:

"{student_answer}"
"""

    try:
      response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    except Exception:
      response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    response_text = response.text.strip()

    # Remove markdown code fences if the model adds them.
    if response_text.startswith("```"):
        response_text = response_text.replace("```json", "")
        response_text = response_text.replace("```", "")
        response_text = response_text.strip()

    import json

    return json.loads(response_text)