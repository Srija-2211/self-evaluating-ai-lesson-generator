
import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found. Check your .env file.")

client = genai.Client(api_key=api_key)


def generate_lesson(topic, feedback=None):

    prompt = f"""
    Act as an expert educational content creator.

    Create a beginner-friendly lesson about: {topic}

    Target audience: Students with no prior knowledge.

    Include:
    1. Simple introduction
    2. Important concepts
    3. Real-world examples
    4. Step-by-step explanation
    5. Five practice questions
    6. Summary

    Use simple English and accurate information.
    """

    if feedback:
        prompt += f"""

        IMPORTANT: An earlier version of this lesson failed evaluation.
        Improve the lesson using this feedback:

        {feedback}
        """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
