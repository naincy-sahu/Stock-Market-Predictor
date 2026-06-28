import pandas as pd

def add_moving_average(data):
    data["MA_10"] = data["Close"].rolling(window=10).mean()
    return data