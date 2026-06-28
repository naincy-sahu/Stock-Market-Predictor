import yfinance as yf

def load_data(stock):
    data = yf.download(stock)
    return data