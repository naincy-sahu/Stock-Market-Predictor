
from utils.data_loader import load_data
from utils.preprocessing import preprocess_data
from utils.indicators import add_moving_average

stock = "AAPL"

data = load_data(stock)

data = preprocess_data(data)

data = add_moving_average(data)

print(data.head())