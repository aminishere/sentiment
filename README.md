
# Sentiment Analysis Tool



A machine learning model that classifies reviews as **Positive** or **Negative** using **Naive Bayes (MultinomialNB)**.


## Tech Stack

<img width="50" height="50" alt="image" src="https://github.com/user-attachments/assets/512c027c-320a-4253-920b-afb27042fb70" /> 
<img width="50" height="50" alt="image" src="https://github.com/user-attachments/assets/b586614d-01cf-43d7-a977-4a8910ce2594" />
<img width="50" height="50" alt="image" src="https://github.com/user-attachments/assets/51e9b5f7-e9c4-4a7b-90c4-85b4d349f354" />
<img width="50" height="50" alt="image" src="https://github.com/user-attachments/assets/80ca20c3-b83f-4f80-8028-74275c0421f5" />
<img width="50" height="50" alt="image" src="https://github.com/user-attachments/assets/09b3b596-3471-41b1-8804-9fe5ddfd4192" />


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





## Features

- Preprocessing of text (stopword removal, stemming).  
- Sentiment classification (**Positive / Negative**).  
- Hyperparameter tuning (`alpha` in Naive Bayes).  
- Confusion matrix & accuracy evaluation.  
- Model persistence using **Pickle**.  


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


