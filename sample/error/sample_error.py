import logging
import traceback
from typing import Optional, Any

from sample.error.code import ErrorCode

class SampleError(Exception):
    def __init__(self, error_code: ErrorCode, extra_vars: Optional[Any] = None) -> None:
        self.error_code = error_code
        self.extra_vars = extra_vars
        super(SampleError, self).__init__(error_code.message)
