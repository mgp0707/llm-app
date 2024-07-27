import streamlit as st
import util.googleAPI as lms

st.set_page_config(page_title="Teaching Planner")
st.title("🏫Teaching Planner")
st.write(
    """This page is a demonstration of how you can ask an AI to create a teaching planner, and use it by your means."""
)

input_subject = st.text_area("Enter the subject you are teaching: ")
input_student_age = st.slider("Select the students age", 1, 24, 12, step=1)
input_duration = st.slider("Select the duration (in minutes) of how long you will teach", 1, 60, 30, step=1)

if st.button("Create a teaching planner"):
    if input_subject:
        create_plan = lms.create_teaching_plan(input_subject, input_student_age, input_duration)
        st.success(create_plan)
    else:
        st.warning("Make sure to type what subject you are teaching.")
    