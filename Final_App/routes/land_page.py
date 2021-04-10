import streamlit as st
from routes.interfaces import main_interface


def home_page():

    st.sidebar.number_input("User ID", min_value=0, max_value=100)
    model = st.sidebar.selectbox("Pick a Model or Approach",
                         ("Collaborative-based", "Content-Based", "Hybrid Model"))

    # Main Page
    outputs = main_interface(model_type=model)  # Pass model to interface
