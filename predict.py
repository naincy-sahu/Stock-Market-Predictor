import joblib
import pandas as pd

# Saved model load karo
model = joblib.load("models/saved_model.pkl")

# User input
ma_10 = float(input("Enter 10 Day Moving Average: "))

# DataFrame banao
input_data = pd.DataFrame({
    "MA_10": [ma_10]
})

# Prediction
prediction = model.predict(input_data)

# Result
print("Predicted Closing Price:", prediction[0])import joblib

model = joblib.load("models/saved_model.pkl")

prediction = model.predict([[150]])

print(prediction)print("Predicting Stock Price...")