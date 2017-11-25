import logging

def get_logger(name):
    logger = logging.getLogger(name)
    logger.addHandler(logging.handlers.logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
    return logger
