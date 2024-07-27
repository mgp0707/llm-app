import streamlit as st
import util.googleAPI as lms

st.set_page_config(page_title="Story Generator")
st.title("📚Story generator")
st.write(
    """This page is a demonstration of how you can generate a story by choosing different categories"""
)

input_author = st.text_area("Who is the author of your story: ")
input_choose_genre = st.selectbox("Select the genre of the story:", ("Romance", "Comedy", "Horror", "Tragedy", "Science fiction"))
input_age_level = st.slider("Select how old this story should be for", 1, 100, 18, step=1)

if st.button("Submit"):
    if input_author:
        generate = lms.generate_story(input_author, input_choose_genre, input_age_level)
        st.success(generate)
    else:
        st.warning("Please enter the authors name")
