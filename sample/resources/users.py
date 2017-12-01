import sys
from bson.json_util import dumps
import falcon
from bson.objectid import ObjectId
from mongoengine.errors import ValidationError, OperationError

from sample.extentions.parse_json import parse_json
from sample.extentions.check_auth import check_auth
from sample.db_operator.main import DbOperator
from sample.error.sample_error import SampleError
from sample.error.code import ErrorCode

@falcon.before(check_auth)
class User(object):
    def on_get(self, req, resp, user_id: str) -> None:
        user = DbOperator.get_user(user_id)
        if user:
            resp.body = dumps(user)
        else:
            raise SampleError(error_code=ErrorCode.NOT_FOUND_USER, extra_vars={'user_id': user_id})

    @falcon.before(parse_json)
    def on_put(self, req, resp, user_id: str) -> None:
        user = req.context.get("body")
        try:
            updated = DbOperator.update_user(user_id, user)
            if updated:
                resp.status = falcon.HTTP_200
                resp.body = dumps(updated)
            else:
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

    def on_delete(self, req, resp, user_id: str) -> None:
        try:
            result = DbOperator.delete_user(user_id)
            if result:
                resp.status = falcon.HTTP_204
            else:
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

class Users(object):
    def on_get(self, req, resp) -> None:
        users = DbOperator.get_users()
        resp.body = dumps(users)

    @falcon.before(parse_json)
    def on_post(self, req, resp) -> None:
        user = req.context.get("body")
        try:
            created = DbOperator.create_user(user)
            resp.body = dumps(created)
        except ValidationError:
            raise SampleError(error_code=ErrorCode.INVALID_USER, extra_vars=user)
        except Exception:
            raise SampleError(error_code=ErrorCode.FAILED_CREATE_USER, extra_vars=user)
