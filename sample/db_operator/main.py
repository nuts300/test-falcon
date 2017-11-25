from typing import Optional
import falcon
from sample.db_operator.schemas.users import Users

class DbOperator(object):
    @staticmethod
    def create_user(user_payload: dict) -> str:
        user = Users(**user_payload)
        user.save()
        return user.to_json()

    @staticmethod
    def get_user(user_id: str) -> Optional[str]:
        user = Users.objects(id=user_id).first() # pylint: disable=E1101
        if user:
            return user.to_json()
        return None

    @staticmethod
    def get_users() -> str:
        users = Users.objects.all() # pylint: disable=E1101
        return users.to_json()

    @staticmethod
    def update_user(user_id: str, user_payload: str) -> int:
        result = Users.objects(id=user_id).update_one(**user_payload) # pylint: disable=E1101
        return result

    @staticmethod
    def delete_user(user_id: str) -> int:
        result = Users.objects(id=user_id).delete() # pylint: disable=E1101
        return result
