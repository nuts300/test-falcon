import falcon
import traceback

from sample.logger import getLogger
from sample.error.code import ErrorCode
from sample.error.sample_error import SampleError

logger = getLogger(__name__)

class FinalErrorHandler(object):

    @staticmethod
    def handle(ex, req, resp, params):
        if isinstance(ex, SampleError):
            code = ex.code.name
            message = ex.code.value
            traceback_message = traceback.format_exc()
            logger.error("[code] %s [message] %s %s\n%s" % (code, message, ex.vars, traceback_message))
            raise falcon.HTTPError(ex.status, code=code, title=message, description=traceback_message)
        elif isinstance(ex, falcon.HTTPError):
            code = ex.code
            message = ex.title
            traceback_message = ex.description = traceback.format_exc()
            logger.error("[code] %s [message] %s\n%s" % (code, message, traceback_message))
            raise ex
        else:
            code = ErrorCode.UNEXPECTED_ERROR.name
            message = ErrorCode.UNEXPECTED_ERROR.value
            traceback_message = traceback.format_exc()
            logger.error("[code] %s [message] %s\n%s" % (code, message, traceback_message))
            raise falcon.HTTPError(falcon.HTTP_500, code=code, title=message, description=traceback_message)

