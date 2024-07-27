import streamlit as st
import util.googleAPI as lms

st.set_page_config(page_title="Medical Assistant")
st.title("💉Medical Assistant")
st.write(
    """This page can demonstrate how AI can diagnose you with a condition you have, based on a number of inputs."""
)

if 'chat' not in st.session_state:
    st.session_state.chat = lms.Chat()

input_text = st.text_area("Enter the text: ")

if st.button("Chat with AI!"):
    if input_text:
        response = st.session_state.chat.make_chat(input_text)
        st.success(response)
    else:
        st.warning("Please enter the text")
