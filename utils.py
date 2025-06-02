import json
import os
import streamlit as st
import requests

def load_flashcards(filepath="flashcards.json"):
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return []

def save_flashcards(flashcards, filepath="flashcards.json"):
    with open(filepath,"w") as f:
        json.dump(flashcards, f, indent=4)

'''
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def generate_flashcard(topic):
    prompt = f"Generate 3 flashcards about the topic: {topic}. Format each as Question - Answer."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful flashcard generator."},
            {"role": "user", "content": prompt}
        ]
    )
    result = response.choices[0].message.content

    return result
'''

HF_API_TOKEN = st.secrets["hf_api_token"]
API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

def query_huggingface(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()  # optional: to raise errors if any
    return response.json()

def generate_flashcard(topic):
    prompt = f"Generate 3 flashcards about the topic: {topic}. Format each as Question - Answer."
    output = query_huggingface({"inputs": prompt})
    if isinstance(output, list) and output:
        generated_text = output[0].get('generated_text', 'No response')
    else:
        generated_text = "No response or error from API"
    return generated_text


def parse_flashcards_from_text(text):
    lines = text.strip().split("\n")
    flashcards = []
    for line in lines:
        if "-" in line:
            q, a = line.split("-", 1)
            flashcards.append({"question": q.strip(), "answer": a.strip(), "tag": ""})
    return flashcards