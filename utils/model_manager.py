import joblib
from utils.logger import logger

def save_model(model, path):
    try:
        joblib.dump(model, path)
        logger.info(f"Model saved successfully at {path}")
    except Exception as e:
        logger.error(f"Error saving model: {e}")

def load_model(path):
    try:
        model = joblib.load(path)
        logger.info(f"Model loaded successfully from {path}")
        return model
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        return None