import pandas as pd

def preprocess_data(data):
    data = data.dropna()
    return data