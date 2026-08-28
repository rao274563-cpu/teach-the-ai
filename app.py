import streamlit as st
from ai_student import get_ai_student_response
from reasoning import analyze_reasoning
from learner_model import LearnerModel
from adaptation import get_next_challenge

learner = LearnerModel()

if "challenge" not in st.session_state:
    st.session_state.challenge = (
        "My model has 99% training accuracy, "
        "so must be a very good model. Do you agree?"
    )


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
    f"""
    🤖 AI Student:

    "{st.session_state.challenge}"
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
                ai_response = get_ai_student_response(
                    answer,
                    st.session_state.challenge
                )

                st.success("The AI student responded:")
                st.write(ai_response)

                reasoning_result = analyze_reasoning(answer)
                score = (
                    reasoning_result["concept_understanding"]
                    + reasoning_result["reasoning_quality"]
                    + reasoning_result["generalization"]
                )/3
                learner.update_mastery(score)

                st.subheader("Your Reasoning Analysis")

                st.write(
                    f"**Concept Understanding:** {reasoning_result['concept_understanding']}/100"
                )

                st.write(
                    f"**Reasoning Quality:** {reasoning_result['reasoning_quality']}/100"
                )

                st.write(
                    f"**Generalization:** {reasoning_result['generalization']}/100"
                )

                st.write(
                    f"**Misconception:** {reasoning_result['misconception']}"
                )

                st.info(
                    f"**Feedback:** {reasoning_result['feedback']}"
                )

                st.subheader("📊 Learner State")
                st.write(f"**Mastery:** {learner.mastery:.0f}/100")
                st.write(f"**Level:** {learner.get_level()}")

                challenge = get_next_challenge(learner.mastery)

                st.session_state.challenge = challenge
                
                st.subheader("🎯 Next Challenge")
                st.write(challenge)

            except Exception as e:
                st.error("Something went wrong while contacting the AI student.")
                st.caption(str(e))

    else:
        st.warning("Please explain your reasoning first.")