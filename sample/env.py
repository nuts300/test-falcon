import os

DEFAULT_DB_HOST = "mongodb://localhost"
DEFAULT_DB_PORT = 27017

# pylint: disable=W0703
def is_production() -> bool:
    try:
        return os.environ['SAMPLE_APP_PRODUCTION'] == "true"
    except KeyError:
        return False

def get_db_host() -> str:
    return DEFAULT_DB_HOST

def get_db_port() -> int:
    return DEFAULT_DB_PORT
