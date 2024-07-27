import streamlit as st

st.header('📆Day 7')

options = st.multiselect(
    'What are your favourite colours',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)
