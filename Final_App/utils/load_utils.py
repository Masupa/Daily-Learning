import pandas as pd


def data():
    data_dir = "./data/data.csv"
    data_frame = pd.read_csv(data_dir)

    return data_frame


def matrix_data():
    data_dir = "./data/collaborative_dataset.csv"
    data_mat = pd.read_csv(data_dir)

    return data_mat


# Original DataFrame
data_frame_ = data()

# Matrix DataFrame - Used for collaborative-filtering
matrix_col = matrix_data()
