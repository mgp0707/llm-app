import streamlit as st

st.header('📆Day 8')

st.write('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
    st.write("Great, here is some ice cream! 🍦")

if coffee:
    st.write("Great, here is some coffee! ☕")

if cola:
    st.write("Great, here is some cola! 🥤")