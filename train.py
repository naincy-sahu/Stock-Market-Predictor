from config import STOCK, TEST_SIZE

from utils.data_loader import load_data
from utils.preprocessing import preprocess_data
from utils.indicators import add_moving_average
from utils.feature_engineering import create_features

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

import joblib

stock = STOCK

# Load Data
data = load_data(stock)

# Clean Data
data = preprocess_data(data)

# Add Moving Average
data = add_moving_average(data)

# Create Extra Features
data = create_features(data)

# Remove Missing Values
data = data.dropna()

# Input Feature 
    X = data[
    [
        "Open",
        "High",
        "Low",
        "Volume",
        "MA_10",
        "Daily_Return",
        "Price_Range",
        "Open_Close_Diff",
        "Volume_Change",
        "EMA_10",
        "MACD"
    ]
]
# Target
y = data["Close"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=TEST_SIZE,
    random_state=42
)

# Create Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train Model
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, predictions)

print("Mean Absolute Error:", mae)

# Save Model
joblib.dump(model, "models/saved_model.pkl")

print("Model Saved Successfully")