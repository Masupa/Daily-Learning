import streamlit as st

# Local Imports
from routes.land_page import home_page
from utils.load_utils import data
from utils.load_utils import matrix_data


def main():

    # Load Data
    data()
    matrix_data()

    # Home Page
    home_page()


if __name__ == '__main__':
    main()
