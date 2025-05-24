# predict.py

import joblib

# Load model
model = joblib.load('phishing_model.pkl')

# Example messages
messages = [
    "Click here to get a free iPhone!",
    "Team meeting rescheduled to 3 PM",
    "Confirm your email to avoid account suspension"
]

# Make predictions
predictions = model.predict(messages)

for msg, pred in zip(messages, predictions):
    result = "Phishing" if pred == 1 else "Not Phishing"
    print(f"Message: {msg}\nPrediction: {result}\n") 
