import nltk_setup
import streamlit as st
import pickle 
import nltk
import nltk.corpus
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

tfdif = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

def transform_text(text):
    text = text.lower() # Lowercase the text
    text = nltk.word_tokenize(text) # Tokenize the text
    y = [] # Create an empty list to store the alphanumeric characters
    for i in text:
        if i.isalnum():
            y.append(i) # Append the alphanumeric characters to the list
    text = y[:] # Create a copy of the list
    y.clear() # Clear the list
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear() 
    ps = PorterStemmer() # Create a PorterStemmer object
    for i in text:
        y.append(ps.stem(i))
    return ' '.join(y) # Join the list of words into a string and return it

if st.button("Predict"):
# Preprocess
    transformed_sms = transform_text(input_sms)

# Vectorize
    vector_input = tfdif.transform([transformed_sms])

# Predict
    result = model.predict(vector_input)[0]

    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
