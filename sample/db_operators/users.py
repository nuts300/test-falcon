import falcon
from mongoengine.errors import ValidationError
from sample.db_operators.documents.user import UserDocument
from sample.error.sample_error import SampleError
from sample.error.code import ErrorCode

class UsersOperator(object):
    def createUser(user):
        try:
            user = UserDocument(**user)
            user.save()
            return user.to_json()
        except ValidationError as err:
            message = "Invalide user payload %s" % (user)
            raise SampleError(status=falcon.HTTP_400, code=ErrorCode.INVALID_USER.name, message=ErrorCode.INVALID_USER.value, exception=err)
        except Exception as err:
            message = "Failed create User %s" % (user)
            raise SampleError(status=falcon.HTTP_500, code=ErrorCode.FAILED_CREATE_USER.name, message=ErrorCode.FAILED_CREATE_USER.value, exception=err)
        
    def getUser(id):
        user = UserDocument.objects(id=ObjectId(id))
        return user.to_json()

    def getUsers():
        users =UserDocument.objects.all()
        return users.to_json()