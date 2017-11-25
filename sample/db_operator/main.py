import falcon
from sample.db_operator.schemas.users import Users

class DbOperator(object):
    @staticmethod
    def create_user(user_payload):
        user = Users(**user_payload)
        user.save()
        return user.to_json()

    @staticmethod
    def get_user(user_id):
        user = Users.objects(id=user_id).first() # pylint: disable=E1101
        if user:
            return user.to_json()
        return None

    @staticmethod
    def get_users():
        users = Users.objects.all() # pylint: disable=E1101
        return users.to_json()

    @staticmethod
    def update_user(user_id, user_payload):
        result = Users.objects(id=user_id).update_one(**user_payload) # pylint: disable=E1101
        return result
