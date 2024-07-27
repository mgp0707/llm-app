import streamlit as st
import util.googleAPI as lms

st.set_page_config(page_title="Note Summarizer")
st.title("📝Note Summarizer")
st.write(
    """This page is a demonstration of how you can paste your notes from work and allow it to be summarized
    so that it is easy to understand"""
)

input_note = st.text_area("Enter the note: ")
input_bulletpoint = st.checkbox("Bullet point")
input_bulletpoint = "Bullet Point" if input_bulletpoint else "No Bullet Point"
input_choose_category = st.selectbox("Select the category of the summaries you want:", ("Summarize each paragraph", "Summarize as a whole"))
input_age = st.slider("Select your age", 1, 100, 18, step=1)

if st.button("Submit"):
    if input_note:
        summary = lms.summarize_text(input_note, input_bulletpoint, input_choose_category, input_age)
        st.success(summary)
    else:
        st.warning("Please enter the notes")
