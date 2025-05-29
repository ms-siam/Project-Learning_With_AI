import streamlit as st
from utils import load_flashcards, save_flashcards, generate_flashcard
import json

flashcards = load_flashcards()

st.title("📚 Learn with AI - Flashcard App")

st.subheader("➕ Add a New Flashcard")
ques = st.text_input('Enter a question')
ans = st.text_area('Enter an answer')

if st.button('Add Flashcard'):
    flashcards.append({"question": ques, "answer": ans})
    save_flashcards(flashcards)
    st.success("Flashcard added!")

st.subheader("📘 Existing Flashcards")
for i, card in enumerate(flashcards):
    with st.expander(f"Question {i+1}: {card[ques]}"):
        st.write(f"**Answer:** {card[ans]}")

st.subheader("🤖 Generate Flashcard from Topic")
topic = st.text_input('Enter a topic')
if st.button('Generate AI Flashcard'):
    ai_ques, ai_ans = generate_flashcard(topic)
    st.write(f"**Question:** {ai_ques}")
    st.write(f"**Answer:** {ai_ans}")
    flashcards.append({"question": ai_ques, "answer": ai_ans})
    save_flashcards(flashcards)
    st.success("AI-generated flashcard added!")