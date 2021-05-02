import re
import string
import nltk
from html.parser import HTMLParser
from nltk.corpus import stopwords

# Load tokenizer
pickle_n = open("./Models/tokenizer.pickle", "rb")
tokenizer = pickle.load(pickle_n)

# Load Model
pickle_in = open("./Models/kmeans_model.sav", "rb")
model = pickle.load(pickle_in)

def clean_enc_text(text):
    clean_text_ = clean_texts(text_input)
    enc_text_ = tokenizer.texts_to_sequences([clean_text_])

    max_length = 2
    padded_text = pad_sequences(enc_text_, maxlen=max_length, padding='post')
    return padded_text


# Function turning a list into a string
def listToString(s):
    str1 = " "
    return (str1.join(s))


# Function to clean texts
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
