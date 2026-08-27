import streamlit as st

st.set_page_config(
    page_title = "Teach the AT",
    page_icon = "🧠",
    layout = "centered"
)

st.title("🧠 Teach the AI")
st.subheader("Machine Learning - Learn by Teaching")

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
    placeholder = "Explain your reasoning..."
)

if st.button("Teach the AI"):
    if answer.strip():
        st.success("Your explanation has been recorded.")
        st.write("Your response:", answer)
    else:
        st.warning("Please explain your reasoning first.")    