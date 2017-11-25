import logging
import falcon
import traceback

from sample.logger import getLogger
from sample.error.code import ErrorCode

logger = getLogger(__name__)

class SampleError(Exception):
    def __init__(self, error_code:ErrorCode, vars):
        self.error_code = error_code
        self.vars = vars

    