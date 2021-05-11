import pandas as pd
import random


def data():
    data_dir = "./data/data.csv"
    data_frame = pd.read_csv(data_dir)

    return data_frame


def matrix_data():
    data_dir = "./data/matrix_dataset.csv"
    data_mat = pd.read_csv(data_dir).set_index("Unnamed: 0")

    return data_mat


def load_matrix():
    random_list = []
    for i in range(0, 5):
        n = random.randint(0, 400)
        random_list.append(n)

    data_dir = "./data/matrix_dataset.csv"
    data_mat = pd.read_csv(data_dir).set_index("Unnamed: 0")

    return random_list


# Original DataFrame
data_frame_ = data()

# Matrix DataFrame - Used for collaborative-filtering
matrix_col = matrix_data()
