Customer Campaign Response Predictor

A machine learning project that predicts whether a customer will respond positively to a marketing campaign based on their demographic and shopping behavior.

>Project Overview

This project uses a Support Vector Machine (SVM) classifier to analyze customer details and predict campaign response (1 = Will Respond, 0 = Not Likely).
A clean and interactive Streamlit web app allows users to input customer information and get predictions instantly.

>Features

Clean, balanced dataset for binary classification

Preprocessing with scaling + encoding

Model comparison (Logistic Regression, Random Forest, SVM, XGBoost)

Final model: SVM (~80% accuracy)

User-friendly Streamlit UI

Dark-blue shopping theme + sidebar navigation

>ML Workflow

EDA & Cleaning

Balancing target classes (333 each)

Train–Test Split

Preprocessing pipeline (StandardScaler + OneHotEncoder)

Model training + evaluation

SVM model saved using joblib

Streamlit app for predictions

> Run the Model Locally
git clone https://github.com/nishthaq3/customer_campaign_predictor.git
cd customer_campaign_predictor
pip install -r requirements.txt
streamlit run app/app.py

> Tech Stack

Python

Pandas

Scikit-learn

XGBoost

Streamlit

📬 Contact

Nishtha Tripathi
nishthatripathi05@gmail.com
LinkedIn: https://www.linkedin.com/in/nishtha-tripathi-0a1925296/
