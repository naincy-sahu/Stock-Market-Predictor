import pandas as pd
import numpy as np

def create_features(data):

    data["Daily_Return"] = data["Close"].pct_change()

    data["Price_Range"] = data["High"] - data["Low"]

    data["Open_Close_Diff"] = data["Close"] - data["Open"]

    data["Volume_Change"] = data["Volume"].pct_change()

    data["EMA_10"] = data["Close"].ewm(
        span=10,
        adjust=False
    ).mean()

    return data