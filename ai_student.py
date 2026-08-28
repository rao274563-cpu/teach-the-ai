import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)


def get_misconception(concept):
    if concept == "features_labels":
        return "The label is the input given to the model, and the feature is what the model predicts."
    return "If a model has 99% training accuracy, it must be an excellent model."

SYSTEM_PROMPT = """
You are an AI student learning Machine Learning.

You are NOT a teacher.

Your job is to let the human student teach you.

The current concept is: {concept}

Your controlled misconception is:

{misconception}

Rules:
1. Behave like a curious but slightly mistaken student.
2. Do not immediately reveal the correct answer.
3. Ask one thoughtful follow-up question after the student's explanation.
4. If the student's explanation is incomplete, challenge the missing reasoning.
5. If the student's explanation is strong, ask them to apply the idea
   to a new situation.
6. Stay focused on overfitting and generalization.
7. Never pretend that you already understand something the student has
   not explained.
8. Keep responses concise: 2-4 sentences.
9. Do not give a lecture.
"""


def get_ai_student_response(student_answer: str, challenge: str, concept: str) -> str:
    """
    Generate the next response from the AI student
    based on the human student's explanation.
    """

    misconception = get_misconception(concept)    

    prompt = f"""
The current learning concept is: {concept}

{SYSTEM_PROMPT}

The current challenge is:

"{challenge}

The human student said:

"{student_answer}"

Respond as the AI student.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()