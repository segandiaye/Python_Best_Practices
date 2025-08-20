from loguru import logger

# import logging

# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def divide(a: int, b: int) -> None:
    logger.info(f"Dividing {a} by {b}")
    try:
        return a / b
    except ZeroDivisionError:
        logger.error("Division by zero attempted")
        raise
