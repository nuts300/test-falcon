import falcon
import traceback

from sample.logger import getLogger
from sample.error.code import ErrorCode

logger = getLogger(__name__)

class FinalErrorHandler(object):

    @staticmethod
    def handle(ex, req, resp, params):
        if not isinstance(ex, falcon.HTTPError):
            code = ErrorCode.UNEXPECTED_ERROR.name
            message = ErrorCode.UNEXPECTED_ERROR.value
            traceback_message = traceback.format_exc()
            logger.error("[code] %s [message] %s %s" % (code, message, traceback_message))
            raise falcon.HTTPError(falcon.HTTP_500, code=code, title=message, description=traceback_message)
