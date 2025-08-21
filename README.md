
# Sentiment Analysis Tool

**About** :  

A machine learning model that classifies reviews as **Positive** or **Negative** using **Naive Bayes (MultinomialNB)**.


## Directory Structure :

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
├── app.py     
├── requirements.txt  
├── README.md  
├── .gitignore
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
