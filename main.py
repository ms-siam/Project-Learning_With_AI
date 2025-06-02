import streamlit as st
from utils import (
    load_flashcards,
    save_flashcards,
    generate_flashcard,
    parse_flashcards_from_text,
)
import json

flashcards = load_flashcards()

st.title("📚 Learn with AI - Flashcard App")

st.subheader("➕ Add a New Flashcard")
ques = st.text_input('Enter a question')
ans = st.text_area('Enter an answer')
tag = st.text_input("Category (e.g., Math, English, Physics)")

if st.button('Add Flashcard'):
    flashcards.append({"question": ques, "answer": ans, "tag": tag})
    save_flashcards(flashcards)
    st.success("Flashcard added!")

st.subheader("📘 Existing Flashcards")
for i, card in enumerate(flashcards):
    with st.expander(f"Question {i+1}: {card['question']}"):
        st.markdown(f"**Answer:** {card['answer']}")
        st.markdown(f"**Category:** {card.get('tag', 'None')}")


st.markdown("### 📚 Generate Flashcards with AI")
topic = st.text_input('Enter a topic')

if st.button('Generate AI Flashcard'):
    if topic:
        result = generate_flashcard(topic)
        st.text_area("Generated Flashcards", result, height=200)

        # Parse and save
        new_flashcards = parse_flashcards_from_text(result)
        for fc in new_flashcards:
            fc["tag"] = topic  # Add the topic as tag/category
        flashcards.extend(new_flashcards)
        save_flashcards(flashcards)

        st.success(f"{len(new_flashcards)} AI flashcards saved!")
    else:
        st.warning("Please enter a topic first.")
    

