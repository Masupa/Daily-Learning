import streamlit as st
from routes.interfaces import main_interface


def home_page():

    user_id = st.sidebar.number_input("User ID", min_value=0, max_value=10000)

    # Main Page
    outputs = main_interface()
