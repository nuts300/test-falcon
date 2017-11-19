from sample.db_operators.documents.user import UserDocument
from sample.error.sample_error import SampleError

class UsersOperator(object):
    def createUser(user):
        try:
            user = UserDocument(**user)
            user.save()
            return user.to_json()
        except Exception as err:
            raise SampleError(status=400, code="TEST_CODE", message="test message", exception=err)
        
    def getUser(id):
        user = UserDocument.objects(id=ObjectId(id))
        return user.to_json()

    def getUsers():
        users =UserDocument.objects.all()
        return users.to_json()