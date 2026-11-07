
import json
from google import genai


def evaluate_lesson(client, topic, lesson):

    prompt = f"""
    You are an expert educational content evaluator.

    Evaluate this lesson about: {topic}

    LESSON:
    {lesson}

    Check these 6 criteria:
    1. Accuracy: Is the information correct?
    2. Clarity: Is the language easy to understand?
    3. Completeness: Are important concepts covered?
    4. Structure: Is the lesson properly organized?
    5. Examples: Are useful examples included?
    6. Beginner-friendly: Can a beginner understand it?

    Give each criterion a score from 1 to 5.

    Pass only if every criterion scores at least 4.

    Return ONLY valid JSON in this format:
    {{
        "scores": {{
            "accuracy": 5,
            "clarity": 4,
            "completeness": 4,
            "structure": 5,
            "examples": 4,
            "beginner_friendly": 5
        }},
        "passed": true,
        "feedback": "Explanation of evaluation"
    }}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return json.loads(response.text)

import json
import re

def evaluate_lesson(client, topic, lesson):
    prompt = f"""
You are an expert educational content evaluator.

Evaluate this beginner-friendly lesson about: {topic}

LESSON:
{lesson}

Check these six criteria:
1. Accuracy
2. Clarity
3. Completeness
4. Structure
5. Examples
6. Beginner-friendly

Give each criterion a score from 1 to 5.
Pass only if every criterion scores at least 4.

Return valid JSON only, using this exact structure:
{{
    "scores": {{
        "accuracy": 5,
        "clarity": 4,
        "completeness": 4,
        "structure": 5,
        "examples": 4,
        "beginner_friendly": 5
    }},
    "passed": true,
    "feedback": "Explanation of evaluation"
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    if not response.text:
        raise ValueError("Gemini returned an empty evaluation response.")

    text = response.text.strip()

    # Remove Markdown code fences if Gemini includes them
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)

    result = json.loads(text)

    required_scores = [
        "accuracy",
        "clarity",
        "completeness",
        "structure",
        "examples",
        "beginner_friendly"
    ]

    for criterion in required_scores:
        if criterion not in result["scores"]:
            raise ValueError(f"Missing evaluation score: {criterion}")

    return result
