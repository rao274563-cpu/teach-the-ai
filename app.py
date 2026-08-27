import streamlit as st
from ai_student import get_ai_student_response


st.set_page_config(
    page_title="Teach the AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Teach the AI")
st.subheader("Machine Learning — Learn by Teaching")

st.write(
    """
    Welcome! In this learning experience, you are not simply answering
    questions. You are teaching an AI student.
    """
)

st.info(
    """
    🤖 AI Student:

    "My model has 99% training accuracy, so it must be a very good model.
    Do you agree?"
    """
)

answer = st.text_area(
    "Teach the AI:",
    placeholder="Explain your reasoning...",
    height=150
)

if st.button("Teach the AI"):
    if answer.strip():
        with st.spinner("The AI student is thinking..."):
            try:
                ai_response = get_ai_student_response(answer)

                st.success("The AI student responded:")
                st.write(ai_response)

            except Exception as e:
                st.error("Something went wrong while contacting the AI student.")
                st.caption(str(e))

    else:
        st.warning("Please explain your reasoning first.")