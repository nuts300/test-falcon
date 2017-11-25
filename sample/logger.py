import logging

def get_logger(name: str):
    logger = logging.getLogger(name)
    if logger.handlers:
        logger.addHandler(logging.handlers.logging.StreamHandler()) # type: ignore
    logger.setLevel(logging.DEBUG)
    return logger
