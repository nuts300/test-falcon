import logging
import falcon
import traceback

from sample.logger import getLogger
from sample.error.code import ErrorCode

logger = getLogger(__name__)

class SampleError(Exception):
    def __init__(self, status, code:ErrorCode, vars):
        self.status = status
        self.code = code
        self.vars = vars

    