import traceback
import falcon

from sample.logger import get_logger
from sample.error.code import ErrorCode
from sample.error.sample_error import SampleError
from sample.env import is_production

LOGGER = get_logger(__name__)

IS_PRODUCTION: bool = is_production()

def final_error_handler(ex, req, resp, params) -> None:
    if isinstance(ex, SampleError):
        code = ex.error_code.name
        message = ex.error_code.message
        status = ex.error_code.status
        traceback_message = traceback.format_exc()
        description = None if IS_PRODUCTION else traceback_message
        LOGGER.error(
            "[code] %s [message] %s %s\n%s", code, message, ex.extra_vars, traceback_message)
        raise falcon.HTTPError(status, code=code, title=message, description=description)
    elif isinstance(ex, falcon.HTTPError):
        code = ex.code
        message = ex.title
        traceback_message = traceback.format_exc()
        LOGGER.error("[code] %s [message] %s\n%s", code, message, traceback_message)
        if (not ex.description) and (not IS_PRODUCTION):
            ex.description = traceback_message
        raise ex
    else:
        code = ErrorCode.UNEXPECTED_ERROR.name
        message = ErrorCode.UNEXPECTED_ERROR.message
        traceback_message = traceback.format_exc()
        description = None if IS_PRODUCTION else traceback_message
        LOGGER.error("[code] %s [message] %s\n%s", code, message, traceback_message)
        raise falcon.HTTPError(
            falcon.HTTP_500, code=code, title=message, description=description)
