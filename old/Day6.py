import streamlit as st

st.header('📆Day 6')

option = st.selectbox(
    "What is your favourite colour?", 
    ("Blue", "Red", "Green"))

st.write('Your favourite colour is ', option)
