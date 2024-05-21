import logging

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('log.txt', 'w', 'utf-8')
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)

def log_message(message):
    logger = logging.getLogger()
    logger.info(message)
