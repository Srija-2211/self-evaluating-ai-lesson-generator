import json
import os

MEMORY_FILE = "rejection_log.json"


def save_rejection(topic, attempt, scores, feedback):

    log = []

    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            log = json.load(file)

    rejection = {
        "topic": topic,
        "attempt": attempt,
        "scores": scores,
        "feedback": feedback
    }

    log.append(rejection)

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(log, file, indent=4)


def get_rejection_history(topic):

    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        log = json.load(file)

    return [
        item for item in log
        if item["topic"].lower() == topic.lower()
    ]
