import streamlit as st
import util.googleAPI as lms

st.set_page_config(page_title="Chatbot")
st.title("Chatbot")
st.write(
    """This page demonstrates how you can chat with AI by using different inputs."""
)

if 'chat' not in st.session_state:
    st.session_state.chat = lms.ChatBot()

user_input = st.text_area("Enter the text: ")

if st.button("Chat with AI!"):
    if user_input:
        response = st.session_state.chat.generate_chat(user_input)
        st.success(response)
    else:
        st.warning("Please enter the text")
