from typing import Optional, List, Any
import falcon
from sample.db_operator.schemas.users import Users

def normalize_mongo_id(byson_obj: dict) -> dict:
    byson_obj["id"] = str(byson_obj["_id"])
    del byson_obj["_id"]
    return byson_obj

# pylint: disable=E1101
class DbOperator(object):
    @staticmethod
    def create_user(user_payload: dict) -> Optional[object]:
        user = Users(**user_payload)
        user.save()
        mongo_obj = user.to_mongo()
        return normalize_mongo_id(mongo_obj)

    @staticmethod
    def get_user(user_id: str) -> Optional[object]:
        user = Users.objects.with_id(user_id)
        if user:
            mongo_obj = user.to_mongo()
            return normalize_mongo_id(mongo_obj)
        return None

    @staticmethod
    def get_users() -> List[Any]:
        users = Users.objects.all()
        mongo_obj_array = [user.to_mongo() for user in users]
        return [normalize_mongo_id(i) for i in mongo_obj_array]

    @staticmethod
    def update_user(user_id: str, user_payload: str) -> Optional[object]:
        Users.objects(id=user_id).update_one(**user_payload)
        user = Users.objects.with_id(user_id)
        if user:
            mongo_obj = user.to_mongo()
            return normalize_mongo_id(mongo_obj)
        return None

    @staticmethod
    def delete_user(user_id: str) -> bool:
        deleted = Users.objects(id=user_id).delete()
        return deleted > 0
