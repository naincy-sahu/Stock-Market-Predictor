import yfinance as yf
from utils.logger import logger

def load_data(stock):
    try:
        logger.info(f"Downloading data for {stock}")

        data = yf.download(stock)

        logger.info("Data Download Successful")

        return data

    except Exception as e:
        logger.error(f"Error: {e}")

        return Noneimport yfinance as yf

def load_data(stock):
    data = yf.download(stock)
    return data