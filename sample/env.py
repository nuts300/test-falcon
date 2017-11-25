import os

DEFAULT_DB_HOST = "mongodb://localhost"
DEFAULT_DB_PORT = 3001

# pylint: disable=W0703
def is_production() -> bool:
    try:
        return os.environ['SAMPLE_APP_PRODUCTION'] == "true"
    except KeyError:
        return False

def get_db_host() -> str:
    try:
        if os.environ["SAMPLE_APP_DB_HOST"]:
            return os.environ["SAMPLE_APP_DB_HOST"]
        return DEFAULT_DB_HOST
    except KeyError:
        return DEFAULT_DB_HOST

def get_db_port() -> int:
    try:
        if os.environ["SAMPLE_APP_DB_PORT"]:
            return int(os.environ["SAMPLE_APP_DB_PORT"])
        return DEFAULT_DB_PORT
    except KeyError:
        return DEFAULT_DB_PORT
