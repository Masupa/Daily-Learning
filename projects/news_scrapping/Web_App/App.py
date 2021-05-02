import pickle
import pandas as pd
import streamlit as st

# ====================================
# Helper Modules
import re
import string
import nltk
from html.parser import HTMLParser
from nltk.corpus import stopwords

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# ====================================
# Helper Modules

# Load tokenizer
pickle_n = open("../Models/tokenizer.pickle", "rb")
tokenizer = pickle.load(pickle_n)

# Load Model
pickle_in = open("../Models/kmeans_model.sav", "rb")
model = pickle.load(pickle_in)

# Load Data
data = pd.read_csv("../Models/url_data.csv")

# Cluster Data
clusters_data = pd.read_csv("../Models/cluster_file.csv")


def clean_enc_text(text):
    clean_text_ = clean_texts(text_input)
    enc_text_ = tokenizer.texts_to_sequences([clean_text_])

    max_length = 2
    padded_text = pad_sequences(enc_text_, maxlen=max_length, padding='post')
    preds = model.predict(padded_text)
    return preds


def listToString(s):
    str1 = " "
    return (str1.join(s))


def clean_texts(text):
    # Removing html characters
    text = HTMLParser().unescape(text)

    # Removing urls and hashtags
    text = re.sub(r'https?:\/\/.\S+', "", text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'^RT[\s]+', '', text)

    # Contradiction replacement
    dictionary = {"'s": " is", "n't": " not", "'m": " am", "'ll": " will",
                  "'d": " would", "'ve": " have", "'re": " are", "\n": " "}

    for key, value in dictionary.items():
        if key in text:
            text = text.replace(key, value)
    # Convert to lower case
    text = text.lower()

    # Removing stopwords
    nltk.download('stopwords')
    stopwords_eng = stopwords.words('english')
    text_tokens = text.split()
    text_list = []
    for word in text_tokens:
        if word not in stopwords_eng:
            text_list.append(word)

    # Remove punctuations
    clean_text = []
    for word in text_list:
        if word not in string.punctuation:
            clean_text.append(word)

    # Turning the list of words into a single string
    clean_text = listToString(clean_text)
    return clean_text


def get_url(pred):

    print(pred)
    print("I am here")

    if pred == 0:
        filter = data['Section'] == "Business"
    elif pred == 1:
        filter = data['Section'] == "Culture"
    elif pred == 2:
        filter = data['Section'] == "Lifestyle"
    elif pred == 3:
        filter = data['Section'] == "Politics"
    elif pred == 4 or pred == 5:
        if pred == 4:
            filter = data['Section'] == "Sport"
        else:
            filter = data['Section'] == "Sports"
    else:
        filter = data['Section'] == "Travel"

    return data[filter][['Title', 'Article_URL']]


# Title
st.markdown("<h1 style='text-align: center; color: \
black;'>NEWSPAPER CLUSTERING APP</h1>", unsafe_allow_html=True)

# Subtitle
st.text("")
st.markdown("<h3 style='text-align: center; color: \
black;'>In the text box below, enter text to receive urls with similar content</h3>", unsafe_allow_html=True)

# Text Field
text_input = st.text_area('Enter article text here!')

# Button
if st.button('Cluster article!'):

    section_pred = clean_enc_text(text=text_input)[0]
    results = get_url(pred=section_pred)

    st.dataframe(results)
