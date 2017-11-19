import logging
import falcon
import traceback

from sample.logger import getLogger

logger = getLogger(__name__)

class SampleError(Exception):
    def __init__(self, exception, status, code, message):
        self.exception = exception
        self.status = status
        self.code = code
        self.message = message

    @staticmethod
    def handle(ex, req, resp, params):
        logger.error("[code] %s [message] %s\n%s" % (ex.code, ex.message, traceback.format_exc()))
        raise falcon.HTTPError(ex.status, code=ex.code, title=ex.message, description=traceback.format_exc())
    