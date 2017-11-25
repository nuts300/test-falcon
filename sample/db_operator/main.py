import falcon
from bson.objectid import ObjectId
from sample.db_operator.documents.user import UserDocument

class DbOperator(object):
    @staticmethod
    def create_user(user_payload):
        user = UserDocument(**user_payload)
        user.save()
        return user.to_json()

    @staticmethod
    def get_user(user_id):
        user = UserDocument.objects(id=ObjectId(user_id)) # pylint: disable=E1101
        return user.to_json()

    @staticmethod
    def get_users():
        users = UserDocument.objects.all() # pylint: disable=E1101
        return users.to_json()
