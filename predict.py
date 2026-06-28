

 import joblib
import pandas as pd

model = joblib.load("models/saved_model.pkl")

ma_10 = float(input("Enter 10 Day Moving Average: "))

input_data = pd.DataFrame({
    "MA_10": [ma_10]
})

prediction = model.predict(input_data)

print("Predicted Closing Price:", prediction[0])