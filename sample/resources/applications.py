import sys
from bson.json_util import dumps
import falcon
from mongoengine.errors import ValidationError, OperationError, NotUniqueError

from sample.extentions.parse_json import parse_json
from sample.db_operator.main import DbOperator
from sample.error.sample_error import SampleError
from sample.error.code import ErrorCode

class Applications(object):

    @falcon.before(parse_json)
    def on_post(self, req, resp) -> None:
        application = req.context.get('body')
        application_id = application.get('application_id')
        password = application.get('password')
        admin = application.get('admin')
        try:
            created = DbOperator.register_application(
                application_id=application_id, password=password, admin=admin)
            resp.body = dumps(created)
        except ValidationError:
            raise SampleError(
                error_code=ErrorCode.INVALID_APPLICATION, extra_vars=application)
        except NotUniqueError:
            raise SampleError(
                error_code=ErrorCode.APPLICATION_ID_DEPLICATED, extra_vars=application)
        except:
            raise SampleError(
                error_code=ErrorCode.FAILED_CREATE_APPLICATION, extra_vars=application)
