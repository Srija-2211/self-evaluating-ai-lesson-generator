
# Self-Evaluating AI Lesson Generator

## Project Overview
An AI-powered lesson generator that creates beginner-friendly educational content and evaluates its quality using an AI evaluator.

## Features
- Generates lessons using Google Gemini.
- Evaluates lessons against six quality criteria.
- Regenerates failed lessons using evaluator feedback.
- Supports up to two retries.
- Saves rejected attempts in a JSON memory file.
- Saves the final approved lesson as Markdown.

## Evaluation Criteria
1. Accuracy
2. Clarity
3. Completeness
4. Structure
5. Examples
6. Beginner-friendly explanation

## Technology Stack
- Python
- Google Gemini API
- JSON
- python-dotenv

## Setup Instructions
1. Clone this repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Create a `.env` file and add your Gemini API key:
   `GEMINI_API_KEY=your_api_key`
4. Run the application:
   `python main.py`

## Output
- `final_lesson.md` – Approved lesson.
- `rejection_log.json` – Evaluation failure history.
