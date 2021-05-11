import streamlit as st
import utils.helper_functions as hf


def recommendation_section(data, title):
    # Adding some space
    st.text("")
    st.text("")

    # Sub-heading
    st.subheader(title)

    # Images
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:  # First book recommended
        st.image(data['Images'][0], width=100)
    with col2:  # Second book recommended
        st.image(data['Images'][1], width=100)
    with col3:  # Third
        st.image(data['Images'][2], width=100)
    with col4:  # Fourth
        st.image(data['Images'][3], width=100)
    with col5:  # Fifth
        st.image(data['Images'][4], width=100)

    # Titles
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:  # First book recommended
        st.markdown(data['Titles'][0])
    with col2:  # Second book recommended
        st.markdown(data['Titles'][1])
    with col3:  # Third
        st.markdown(data['Titles'][2])
    with col4:  # Fourth
        st.markdown(data['Titles'][3])
    with col5:  # Fifth
        st.markdown(data['Titles'][4])


def main_interface():
    st.header("BOOK RECOMMENDATION ENGINE")

    st.text("")
    st.text("")

    # Book Name
    st.markdown("""We know you love reading. What books have you previously read? We can help you find similar ones!""")

    book_name = st.text_input('')

    st.text("")
    st.image("https://images.unsplash.com/photo-1512820790803-83ca734da794?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB\
    8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1548&q=80", width=700)

    # Button
    button_clicked = st.button("Browse similar books")

    pass_data = {
        'Book_name': book_name,
        'Button_clicked': button_clicked
    }

    # Button has been clicked
    if button_clicked:

        # Getting the most frequest books
        freq_books_ = hf.most_freq_books()
        recommendation_section(data=freq_books_, title="Pick in the most frequent read books")

        # Getting the highly rated books
        highly_rated_ = hf.highly_rated_books()
        recommendation_section(data=highly_rated_, title="These books were rated high")

        if book_name is not "":
            top_10_books = hf.collaborative_filtering(book_name=book_name)
            recommendation_section(data=top_10_books, title="Here our top 5 recommendations on similar books")
        else:
            st.write("")
            st.write("")
            st.write("")
            st.write("Enter a book for personalised recommendations!")
