import logging
import falcon
import traceback

from sample.logger import getLogger
from sample.error.code import ErrorCode

logger = getLogger(__name__)

class SampleError(Exception):
    def __init__(self, exception, status, code:ErrorCode, vars):
        self.exception = exception
        self.status = status
        self.code = code
        self.vars = vars

    @staticmethod
    def handle(ex, req, resp, params):
        code = ex.code.name
        message = ex.code.value
        traceback_message = traceback.format_exc()
        logger.error("[code] %s [message] %s %s\n%s" % (code, message, ex.vars, traceback_message))
        raise falcon.HTTPError(ex.status, code=code, title=message, description=traceback_message)
    