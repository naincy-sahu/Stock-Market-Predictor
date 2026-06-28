from config import STOCK, TEST_SIZEfrom utils.data_loader import load_data
from utils.preprocessing import preprocess_data
from utils.indicators import add_moving_average

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

stock = STOCK

data = load_data(stock)
data = preprocess_data(data)
data = add_moving_average(data)
data = data.dropna()

X = data[["Open", "High", "Low", "Volume", "MA_10"]]
y = data["Close"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,test_size=TEST_SIZE, random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print("Mean Absolute Error:", mae)

joblib.dump(model, "models/saved_model.pkl")

print("Model Saved Successfully")