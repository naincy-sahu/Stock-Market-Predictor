from utils.data_loader import load_data
from utils.preprocessing import preprocess_data
from utils.indicators import add_moving_average

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

stock = "AAPL"

data = load_data(stock)

data = preprocess_data(data)

data = add_moving_average(data)

data = data.dropna()


X = data[
    [
        "Open",
        "High",
        "Low",
        "Volume",
        "MA_10"
    ]
]

y = data["Close"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

print("Model Training Completed")X = data[
    [
        "Open",
        "High",
        "Low",
        "Volume",
        "MA_10"
    ]
]

y = data["Close"]import joblib
import pandas as pd

# Saved model load karo
model = joblib.load("models/saved_model.pkl")

# User input
ma_10 = float(input("Enter 10 Day Moving Average: "))

# DataFrame 
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