import falcon
from bson.objectid import ObjectId
from sample.db_operator.documents.user import UserDocument

class DbOperator(object):
    @staticmethod
    def createUser(userPayload):
        user = UserDocument(**userPayload)
        user.save()
        return user.to_json()
    
    @staticmethod
    def getUser(id):
        user = UserDocument.objects(id=ObjectId(id))
        return user.to_json()

    @staticmethod
    def getUsers():
        users =UserDocument.objects.all()
        return users.to_json()