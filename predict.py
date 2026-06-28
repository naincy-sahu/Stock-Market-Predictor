import joblib
import pandas as pd

# Trained model load karo
model = joblib.load("models/saved_model.pkl")

# User Input
open_price = float(input("Enter Open Price: "))
high_price = float(input("Enter High Price: "))
low_price = float(input("Enter Low Price: "))
volume = float(input("Enter Volume: "))
ma10 = float(input("Enter 10-Day Moving Average: "))

# DataFrame banao
input_data = pd.DataFrame({
    "Open": [open_price],
    "High": [high_price],
    "Low": [low_price],
    "Volume": [volume],
    "MA_10": [ma10]
})

# Prediction
prediction = model.predict(input_data)

print("Predicted Closing Price:", prediction[0])