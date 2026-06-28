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

X = data[["MA_10"]]

y = data["Close"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

print("Model Training Completed")
from utils.data_loader import load_data
from utils.preprocessing import preprocess_data
from utils.indicators import add_moving_average

stock = "AAPL"

data = load_data(stock)

data = preprocess_data(data)

data = add_moving_average(data)

print(data.head())