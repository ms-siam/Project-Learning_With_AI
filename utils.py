import json
import os

def load_flashcards(filepath="flashcards.json"):
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return []

def save_flashcards(flashcards, filepath="flashcards.json"):
    with open(filepath,"w") as f:
        json.dump(flashcards, f, indent=4)

def generate_flashcard(topic):
    return (f"What is a basic concept of {topic}?"), f"A basic concept of {topic} is that it is important to understand how it works."
