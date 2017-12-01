import sys
from bson.json_util import dumps
import falcon
import bcrypt
import jwt
from mongoengine.errors import ValidationError, OperationError

from sample.extentions.parse_json import parse_json
from sample.db_operator.main import DbOperator
from sample.error.sample_error import SampleError
from sample.error.code import ErrorCode

SECRET = b'SUPER_SECRET'

class Login(object):

    @falcon.before(parse_json)
    def on_post(self, req, resp) -> None:
        application = req.context.get('body')
        application_id = application.get('application_id')
        password = application.get('password')
        application = DbOperator.login_application(application_id=application_id, password=password)
        if application:
            encoded = jwt.encode({'application_id': application['application_id'], 'admin': application['admin']}, SECRET, algorithm='HS256')
            resp.body = dumps({'token': encoded})
        else:
            raise SampleError(error_code=ErrorCode.UNAUTHORIZED, extra_vars={'token': token})
