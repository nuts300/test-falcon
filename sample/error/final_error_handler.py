import traceback
import falcon

from sample.logger import get_logger
from sample.error.code import ErrorCode
from sample.error.sample_error import SampleError

LOGGER = get_logger(__name__)


def final_error_handler(ex, req, resp, params):
    if isinstance(ex, SampleError):
        code = ex.error_code.name
        message = ex.error_code.message
        status = ex.error_code.status
        traceback_message = traceback.format_exc()
        LOGGER.error("[code] %s [message] %s %s\n%s", \
            code, message, ex.extra_vars, traceback_message)
        raise falcon.HTTPError(status, code=code, title=message, description=traceback_message)
    elif isinstance(ex, falcon.HTTPError):
        code = ex.code
        message = ex.title
        traceback_message = traceback.format_exc()
        LOGGER.error("[code] %s [message] %s\n%s", code, message, traceback_message)
        if not ex.description:
            ex.description = traceback_message
        raise ex
    else:
        code = ErrorCode.UNEXPECTED_ERROR.name
        message = ErrorCode.UNEXPECTED_ERROR.message
        traceback_message = traceback.format_exc()
        LOGGER.error("[code] %s [message] %s\n%s", code, message, traceback_message)
        raise falcon.HTTPError(falcon.HTTP_500,\
            code=code, title=message, description=traceback_message)
