import textwrap

import streamlit as st
from chain.llm_chain import generate_answer


st.title("{{ cookiecutter.project_slug }} 🎉")

with st.sidebar:
    with st.form("my_form"):
        question = st.text_area('Ask a question')
        submit = st.form_submit_button('Submit')

if question and submit:
    question = question.strip()
    response = generate_answer(question)
    st.text(textwrap.fill(response, width=80))
