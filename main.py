from generator import generate_lesson, client
from evaluator import evaluate_lesson
from memory import save_rejection, get_rejection_history

MAX_RETRIES = 2

def run_lesson_generator():
    topic = input("Enter your lesson topic: ")
    feedback = None
    final_lesson = None

    previous_failures = get_rejection_history(topic)

    if previous_failures:
        print("Previous evaluation failures found.")
        feedback = previous_failures[-1]["feedback"]

    for attempt in range(MAX_RETRIES + 1):
        print(f"\nGenerating lesson... Attempt {attempt + 1}")

        lesson = generate_lesson(topic, feedback)

        print("Evaluating lesson...")
        result = evaluate_lesson(client, topic, lesson)

        print("\nEvaluation scores:")
        print(result["scores"])

        scores = result["scores"]

        passed = (
            all(int(score) >= 4 for score in scores.values())
            and result["passed"] is True
        )

        if passed:
            final_lesson = lesson
            print("\nLesson passed evaluation!")

            with open("final_lesson.md", "w", encoding="utf-8") as file:
                file.write(lesson)

            break

        feedback = result["feedback"]

        save_rejection(topic, attempt + 1, scores, feedback)

        print("\nLesson failed evaluation.")
        print("Feedback:", feedback)

    if final_lesson:
        print("\nSUCCESS! Final lesson saved in final_lesson.md")
    else:
        print("\nMaximum retries reached.")
        print("No lesson passed evaluation.")


if __name__ == "__main__":
    run_lesson_generator()