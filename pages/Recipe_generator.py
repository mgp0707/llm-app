import streamlit as st
import util.googleAPI as lms

st.set_page_config(page_title="Recipe generator")
st.title("🍳Recipe generator")
st.write(
    """This page is a demonstration of how AI can generate a recipe based on the ingredients you have right now."""
)

ingredients = st.text_area("Which ingredients do you have right now at home: ")
input_time = st.slider("Select the duration of the cooking time (in hours):", 1, 10, 5, step=1)
input_difficulty = st.slider("Select the difficulty of the recipe", 1, 10, 5, step=1)


if st.button("Generate recipe"):
    if ingredients:
        generate = lms.generate_recipe(ingredients, input_time, input_difficulty)
        st.success(generate)
    else:
        st.warning("Please enter your name")
