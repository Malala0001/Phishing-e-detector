# phishing_detector.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Sample data (you can replace this with a CSV file if available)
data = {
    "message": [
        "Update your account info immediately",
        "You have won $10,000 dollars!",
        "Meeting at 2 PM tomorrow",
        "Verify your bank account now",
        "Lunch at 1 PM",
        "Click this link to claim your prize",
        "Let
