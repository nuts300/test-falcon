from typing import Optional, List, Any
import falcon
from sample.db_operator.schemas.users import Users

# pylint: disable=E1101
class DbOperator(object):
    @staticmethod
    def create_user(user_payload: dict) -> Optional[object]:
        user = Users(**user_payload)
        user.save()
        return user.to_mongo()

    @staticmethod
    def get_user(user_id: str) -> Optional[object]:
        return Users.objects.with_id(user_id).to_mongo()

    @staticmethod
    def get_users() -> List[Any]:
        users = Users.objects.all()
        return [user.to_mongo() for user in users]

    @staticmethod
    def update_user(user_id: str, user_payload: str) -> Optional[object]:
        updated = Users.objects(id=user_id).update_one(**user_payload)
        if updated > 0:
            return Users.objects.with_id(user_id).to_mongo()
        return None

    @staticmethod
    def delete_user(user_id: str) -> bool:
        deleted = Users.objects(id=user_id).delete()
        return deleted > 0
