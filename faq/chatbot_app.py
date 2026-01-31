import streamlit as st
from chatbot import get_best_answer

st.title("Mental Health FAQ Chatbot")
st.write("Ask a question related to mental health:")

user_input = st.text_input("Your question")

if user_input:
    answer = get_best_answer(user_input)
    st.success(answer)
