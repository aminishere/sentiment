import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk

# Download stopwords if first time
nltk.download('stopwords')

# Load the saved model & vectorizer
with open("sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Function to clean the text (same as in training)
def preprocess_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    words = text.split()
    words = [w for w in words if w not in set(stopwords.words('english'))]
    ps = PorterStemmer()
    words = [ps.stem(w) for w in words]
    return ' '.join(words)

# Streamlit UI
st.title("📊 Sentiment Analysis App")
st.write("Type a restaurant review and see if it’s Positive or Negative.")

user_input = st.text_area("Enter your review:")

if st.button("Predict Sentiment"):
    if user_input.strip() != "":
        clean_text = preprocess_text(user_input)
        vectorized_text = vectorizer.transform([clean_text]).toarray()
        result = model.predict(vectorized_text)[0]

        if result == 1:
            st.success("✅ Positive Review")
        else:
            st.error("❌ Negative Review")
    else:
        st.warning("Please enter a review before predicting.")
