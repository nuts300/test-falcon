import sys
import falcon
from bson.objectid import ObjectId
from mongoengine.errors import ValidationError, OperationError

from sample.extentions.parse_json import parse_json
from sample.db_operator.main import DbOperator
from sample.error.sample_error import SampleError
from sample.error.code import ErrorCode

class User(object):
    def on_get(self, req, resp, user_id: str):
        result = DbOperator.get_user(user_id)
        if result:
            resp.body = result
        else:
            raise SampleError(error_code=ErrorCode.NOT_FOUND_USER, extra_vars={'user_id': user_id})

    @falcon.before(parse_json)
    def on_put(self, req, resp, user_id: str) -> None:
        user = req.context.get("body")
        try:
            result = DbOperator.update_user(user_id, user)
            if result < 1:
                raise SampleError(
                    error_code=ErrorCode.NOT_FOUND_USER, extra_vars=(user, {'user_id': user_id}))
        except SampleError as error:
            raise error
        except (ValidationError, OperationError):
            raise SampleError(
                error_code=ErrorCode.INVALID_USER, extra_vars=(user, {'user_id': user_id}))
        except Exception:
            raise SampleError(
                error_code=ErrorCode.FAILED_UPDATE_USER, extra_vars=(user, {'user_id': user_id}))
        resp.status = falcon.HTTP_204

    def on_delete(self, req, resp, user_id: str) -> None:
        try:
            result = DbOperator.delete_user(user_id)
            if result < 1:
                raise SampleError(
                    error_code=ErrorCode.NOT_FOUND_USER, extra_vars=({'user_id': user_id}))
        except SampleError as error:
            raise error
        except (ValidationError, OperationError):
            raise SampleError(
                error_code=ErrorCode.INVALID_ID, extra_vars=({'user_id': user_id}))
        except Exception:
            raise SampleError(
                error_code=ErrorCode.FAILED_DELETE_USER, extra_vars=({'user_id': user_id}))
        resp.status = falcon.HTTP_204

class Users(object):
    def on_get(self, req, resp) -> None:
        result = DbOperator.get_users()
        resp.body = result

    @falcon.before(parse_json)
    def on_post(self, req, resp) -> None:
        user = req.context.get("body")
        try:
            result = DbOperator.create_user(user)
        except ValidationError:
            raise SampleError(error_code=ErrorCode.INVALID_USER, extra_vars=user)
        except Exception:
            raise SampleError(error_code=ErrorCode.FAILED_CREATE_USER, extra_vars=user)
        resp.body = result
