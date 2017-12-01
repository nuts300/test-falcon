from typing import Optional, List, Any, Dict
import bcrypt
import falcon
from sample.db_operator.schemas.users import Users
from sample.db_operator.schemas.applications import Applications

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

    @staticmethod
    def register_application(application_id: str, password: str, admin: bool) -> dict:
        password_bytes = password.encode('UTF-8')
        salt = bcrypt.gensalt(rounds=10, prefix=b'2a')
        hash_password = bcrypt.hashpw(password_bytes, salt)
        application = Applications(
            application_id=application_id, password=hash_password, admin=admin)
        application.save()
        return application.to_mongo()

    @staticmethod
    def get_applications() -> List[Dict]:
        applications = Applications.objects.all()
        mongo_obj_array = [application.to_mongo() for application in applications]
        return mongo_obj_array

    @staticmethod
    def get_application(application_id: str) -> Optional[Dict]:
        application = Applications.objects(application_id=application_id).first()
        return application.to_mongo()

    @staticmethod
    def update_application(application_id: str, application_payload: dict) -> Optional[Dict]:
        Applications.objects(application_id=application_id).update_one(**application_payload)
        application = Users.objects(application_id=application_id)
        if application:
            return application.to_mongo()
        return None

    @staticmethod
    def delete_application(application_id: str) -> bool:
        deleted = Applications.objects(application_id=application_id).delete()
        return deleted > 0

    @staticmethod
    def login_application(application_id: str, password: str) -> Optional[Dict]:
        application = Applications.objects(application_id=application_id).first()
        check = bcrypt.checkpw(password.encode('UTF-8'), application['password'].encode('UTF-8'))
        if application and check:
            return application.to_mongo()
        return None
