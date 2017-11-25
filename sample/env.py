import os

# pylint: disable=C0121,W0703
def is_production() -> bool:
    try:
        return os.environ['SAMPLE_APP_PRODUCTION'] == "true"
    except Exception:
        return False
