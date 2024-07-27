import streamlit as st
import util.googleAPI as lms

st.title("Web dev")

# Check if the submit button has been clicked before
if 'submit_clicked' not in st.session_state:
    st.session_state.submit_clicked = False

# Display the text area with session state
input_web_description = st.text_area(
    "Enter the website description: "
)

generated_website = ""

# Handle the submit button click
if st.button("Submit"):
    if input_web_description:
        if not st.session_state.submit_clicked:
            st.session_state.submit_clicked = True

            # Generate the website based on the description
            website_generator = lms.generate_website(input_web_description)
            st.success(website_generator)

            generated_website = website_generator
        else:
            website_generator = lms.improve_website(input_web_description, generated_website)
            generated_website = website_generator

            st.success(website_generator)
    else:
        st.warning("Please enter the description of the website")