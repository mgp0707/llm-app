import streamlit as st
import util.googleAPI as lms

st.set_page_config(page_title="Real Estate Simulation")
st.title("🏠Real Estate Simulation")
st.write(
    """This page is a demonstration of how you can create a house plan simulation by choosing different caterogies"""
)

input_name = st.text_area("What is your name: ")
input_choose_house = st.selectbox("Select the type of house you are looking for:", ("Townhouse", 
                                                                                    "Apartment", "Villas", "State houses"))
input_rich_level = st.slider("Select how old wealthy you are, on a scale of 1 to 10:", 1, 10, 5, step=1)
input_family_members = st.selectbox("Are you planning to live alone or with family:", ("Alone", "Family"))

if st.button("Get your estate plan results here!"):
    if input_name:
        generate = lms.generate_estate_plan(input_name, input_choose_house, input_rich_level, input_family_members)
        st.success(generate)
    else:
        st.warning("Please enter your name")
