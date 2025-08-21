
# Sentiment Analysis Tool

**About** :  

A machine learning model that classifies reviews as **Positive** or **Negative** using **Naive Bayes (MultinomialNB)**.


## Directory Structure :
```
Sentiment-Analysis/  
│  
├── data/  
│ ├── Restaurant_Reviews.tsv  
│  
├── notebooks/  
│ ├── sentiment-ana.ipynb  
│      
├── models/  
│ ├── sentiment_model.pkl   
│ ├── vectorizer.pkl  
│
├── install.sh      
├── app.py     
├── requirements.txt  
├── README.md  
├── .gitignore

```

## Tech Stack

- Python   
- Scikit-learn  -> vectorization, model training, evaluation
- NLTK  -> preprocessing (tokenization, stopwords, stemming)
- NumPy, Pandas  -> data reading
- Matplotlib, Seaborn  -> confusion matrix & visualization


## Features

- Preprocessing of text (stopword removal, stemming).  
- Sentiment classification (**Positive / Negative**).  
- Hyperparameter tuning (`alpha` in Naive Bayes).  
- Confusion matrix & accuracy evaluation.  
- Model persistence using **Pickle**.  

## Deployment

Model deployed on Streamlit.

## Installation Guide

1. Clone the repository:

   ```
    git clone https://github.com/aminishere/sentiment.git
    cd sentiment
   ```
2. Make the installation script executable (in windows use git bash in terminal):

   ```
   chmod +x install.sh
   ```

3. Run the script to install dependencies:

   ```
   ./install.sh
   ```

4. Start the Streamlit app:

   ```
   streamlit run app.py
   ```
