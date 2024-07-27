import streamlit as st
import util.googleAPI as lms
import PIL.Image as Image

if 'images' not in st.session_state:
    st.session_state.images = []

picture_input = st.camera_input("Take a picture")

for images in st.session_state.images:
    st.image(images)

if picture_input:
    st.session_state.images.append(Image.open(picture_input))

if st.button("Submit"):
    if picture_input:
        generate = lms.image_story(st.session_state.images)
        st.success(generate)
    else:
        st.warning("Please take at least one photo!")

