import falcon
from mongoengine.errors import ValidationError
from sample.db_operator.documents.user import UserDocument
from sample.error.sample_error import SampleError
from sample.error.code import ErrorCode

class DbOperator(object):
    @staticmethod
    def createUser(userPayload):
        try:
            user = UserDocument(**userPayload)
            user.save()
            return user.to_json()
        except ValidationError as err:
            raise SampleError(status=falcon.HTTP_400, code=ErrorCode.INVALID_USER, exception=err, vars=userPayload)
        except Exception as err:
            raise SampleError(status=falcon.HTTP_500, code=ErrorCode.FAILED_CREATE_USER, exception=err, vars=userPayload)
    
    @staticmethod
    def getUser(id):
        user = UserDocument.objects(id=ObjectId(id))
        return user.to_json()

    @staticmethod
    def getUsers():
        users =UserDocument.objects.all()
        return users.to_json()