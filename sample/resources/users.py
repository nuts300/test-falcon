import sys
import falcon
from bson.objectid import ObjectId
from mongoengine.errors import ValidationError

from sample.extentions.parse_json import parse_json
from sample.db_operator.main import DbOperator
from sample.error.sample_error import SampleError
from sample.error.code import ErrorCode

class User(object):
    def on_get(self, req, resp, user_id):
        result = DbOperator.get_user(user_id)
        if result:
            resp.body = result
        else:
            raise SampleError(error_code=ErrorCode.NOT_FOUND_USER, extra_vars={'user_id': user_id})

class Users(object):
    def on_get(self, req, resp):
        result = DbOperator.get_users()
        resp.body = result

    @falcon.before(parse_json)
    def on_post(self, req, resp):
        user = req.context.get("body")
        try:
            result = DbOperator.create_user(user)
        except ValidationError:
            raise SampleError(error_code=ErrorCode.INVALID_USER, extra_vars=user)
        except Exception:
            raise SampleError(error_code=ErrorCode.FAILED_CREATE_USER, extra_vars=user)
        resp.body = result
