import streamlit as st
import pandas as pd
from utils.load_utils import data_frame_
from utils.load_utils import matrix_col


def most_freq_books():
    # Aggregate "Book-Title" by how many times a book appears
    book_freq = pd.DataFrame(data_frame_['Book-Title'].value_counts())
    # Reset index
    book_freq.reset_index(inplace=True)
    # Rename columns
    book_freq.columns = ['Book_Title', 'Number of times book was read']

    # ================================================
    # Getting images of books
    freq_books = book_freq.head()['Book_Title'].values
    images = list()

    for book in freq_books:
        images.append(data_frame_[data_frame_['Book-Title'] == book]['Image-URL-L'].iloc[0])

    freq_books_ = {
        'Titles': freq_books,
        'Images': images
    }

    return freq_books_


def highly_rated_books():
    # Filter-out a list of books that were rating more than 50 times
    read_50 = data_frame_['Book-Title'].value_counts()[data_frame_['Book-Title'].value_counts() > 50].index

    # Filtering out books by "read_50"
    book_50 = data_frame_[data_frame_['Book-Title'].isin(read_50)]

    # Group books by "title" and aggregate the mean-rating
    rating_groupby = book_50.groupby(by='Book-Title')[['Book-Rating']].mean()

    # Sort DataFrame
    rating_groupby.sort_values(by='Book-Rating', ascending=False, inplace=True)

    # Reseting index
    rating_groupby.reset_index(inplace=True)

    rating_groupby.head(10)

    highly_rated = rating_groupby.head()['Book-Title'].values

    images = list()

    for book in highly_rated:
        images.append(data_frame_[data_frame_['Book-Title'] == book]['Image-URL-L'].iloc[0])

    highly_rated_ = {
        'Titles': highly_rated,
        'Images': images
    }

    return highly_rated_


def collaborative_filtering(book_name):
    # Similar books
    top_10_similar_books = pd.DataFrame(matrix_col[book_name].sort_values(ascending=False)).iloc[1:]

    books = top_10_similar_books.head(10)

    book_titles = ['Cuentos del Planeta Tierra', 'Dark Lady',
       'Danny the Champion of the World', 'Danger',
       'Dancing at the Rascal Fair: A Novel',
       'Dancing On My Grave Gelsey Kirkland', 'Dances With Wolves',
       'Daisy Fay and the Miracle Man', "Daddy's Little Girl", 'DREAMSNAKE']

    images = list()

    for book in book_titles:
        images.append(data_frame_[data_frame_['Book-Title'] == book]['Image-URL-L'].iloc[0])

    colla_books_ = {
        'Titles': book_titles,
        'Images': images
    }

    return colla_books_

    # for book in books.index:
    #     if book in data_frame_['Book-Title'].values:
    #         print("Yes")
    #     else:
    #         print(data_frame_[data_frame_['User-ID'] == book]['Book-Title'].iloc[0])
