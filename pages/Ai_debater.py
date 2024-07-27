import streamlit as st
import util.googleAPI as lms
st.set_page_config(page_title="Ai debater")
st.title("Ai debater")
st.write(
    """This page demonstrates how you can debate with an AI."""
)

if 'chat' not in st.session_state:
    st.session_state.chat = lms.Debater("Unicorns are real")

debate_topic = st.text_area("Enter the text: ")

if st.button("Debate with AI!"):
    if debate_topic:
        response = st.session_state.chat.generate_chat(debate_topic)
        st.success(response)
    else:
        st.warning("Please enter the text")

if st.button("Evaluate"):
    response = st.session_state.chat.evaluate()
    st.success(response)