#!/bin/bash
echo "Set up the project ->"

#step1
python3 -m venv venv
source venv/bin/activate

#step2
pip install --upgrade pip

#step3
if [-f requirements.txt]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found"
    exit 1
fi        

#step4
if [ -f !sentiment_model.pkl ]; then
    echo "model not found, first train it"
else 
    echo "model exists"
fi

#step5
echo "starting the web UI"
python app.py
