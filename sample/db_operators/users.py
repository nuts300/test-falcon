from mongoengine.errors import ValidationError
from sample.db_operators.documents.user import UserDocument
from sample.error.sample_error import SampleError

class UsersOperator(object):
    def createUser(user):
        try:
            user = UserDocument(**user)
            user.save()
            return user.to_json()
        except ValidationError as err:
            message = "Invalide user payload %s" % (user)
            raise SampleError(status="400", code="INVALID_USER", message=message, exception=err)
        except Exception as err:
            message = "Failed create User %s" % (user)
            raise SampleError(status="500", code="TEST_CODE", message=message, exception=err)
        
    def getUser(id):
        user = UserDocument.objects(id=ObjectId(id))
        return user.to_json()

    def getUsers():
        users =UserDocument.objects.all()
        return users.to_json()