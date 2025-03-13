import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "your_openai_api_key_here"

# User progress tracking (can be replaced with a database)
user_progress = {}

st.title("AI-Based Personalized Learning Tutor")

# Chatbot Functionality
st.header("Ask the AI Tutor")
question = st.text_input("Enter your question:")
if st.button("Get Answer"):
    if question:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an AI tutor helping students."},
                      {"role": "user", "content": question}]
        )
        answer = response["choices"][0]["message"]["content"]
        st.write("**AI Tutor:**", answer)
    else:
        st.warning("Please enter a question.")

# Quiz Generation
st.header("Generate a Quiz")
topic = st.text_input("Enter a topic for the quiz:")
if st.button("Generate Quiz"):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Generate a short quiz on " + topic}]
    )
    quiz = response["choices"][0]["message"]["content"]
    st.write("**Quiz:**", quiz)

# Progress Tracking
st.header("Track Learning Progress")
user_id = st.text_input("Enter User ID:")
score = st.number_input("Enter your score:", min_value=0, max_value=100)
if st.button("Update Progress"):
    if user_id:
        if user_id not in user_progress:
            user_progress[user_id] = []
        user_progress[user_id].append(score)
        st.success(f"Progress Updated! Your scores: {user_progress[user_id]}")
    else:
        st.warning("Please enter a User ID.")
