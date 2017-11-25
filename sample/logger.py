import logging

def get_logger(name):
    logger = logging.getLogger(name)
    if logger.handlers:
        logger.addHandler(logging.handlers.logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
    return logger
