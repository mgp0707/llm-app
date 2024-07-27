import streamlit as st
import util.googleAPI as lms
import PIL.Image as Image

picture = st.camera_input("Take a picture")

question = st.text_area("Enter the question you want to ask about the picture: ")

if picture and question:
    generate_picture_analysis = lms.image_caption(Image.open(picture), question)
    st.success(generate_picture_analysis)
else:
    st.warning("Please enter the question and take the photo.")


