import json
import os
import openai
import streamlit as st

def load_flashcards(filepath="flashcards.json"):
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return []

def save_flashcards(flashcards, filepath="flashcards.json"):
    with open(filepath,"w") as f:
        json.dump(flashcards, f, indent=4)

import streamlit as st
openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_flashcard(topic):
    prompt = f"Generate 3 flashcards about the topic: {topic}. Format each as Question - Answer."
    response = openai.ChatCompletions.create(
        model="gpt-3.5-turbo",  # You can use gpt-4 if you have access
        messages=[
            {"role": "system", "content": "You are a helpful flashcard generator."},
            {"role": "user", "content": prompt}
        ]
    )
    result = response['choices'][0]['message']['content']
    return result

def parse_flashcards_from_text(text):
    lines = text.strip().split("\n")
    flashcards = []
    for line in lines:
        if "-" in line:
            q, a = line.split("-", 1)
            flashcards.append({"question": q.strip(), "answer": a.strip(), "tag": ""})
    return flashcards