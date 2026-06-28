import logging

logging.basicConfig(
    filename="stock_predictor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)