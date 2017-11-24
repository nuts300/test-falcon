import falcon
from bson.objectid import ObjectId
from sample.extentions.parse_json import parseJson
from mongoengine.errors import ValidationError

from sample.db_operator.main import DbOperator
from sample.error.sample_error import SampleError
from sample.error.code import ErrorCode

class User(object):
    def on_get(self, req, resp, id):
        result = DbOperator.getUser(id)
        resp.body = result

class Users(object):
    def on_get(self, req, resp):
        result = DbOperator.getUsers()
        resp.body = result

    @falcon.before(parseJson)
    def on_post(self, req, resp):
        user = req.context.get("body")
        try:
            result = DbOperator.createUser(user)
        except ValidationError as err:
            raise SampleError(status=falcon.HTTP_400, code=ErrorCode.INVALID_USER, exception=err, vars=user)
        except Exception as err:
            raise SampleError(status=falcon.HTTP_500, code=ErrorCode.FAILED_CREATE_USER, exception=err, vars=user)
        resp.body = result
