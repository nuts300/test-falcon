from enum import Enum, unique
import falcon

@unique
class ErrorCode(Enum):
    UNAUTHORIZED = ("Unauthorized", falcon.HTTP_401)
    INVALID_JSON = ("Invalid json", falcon.HTTP_500)
    INVALID_ID = ("Invalid id", falcon.HTTP_400)
    INVALID_USER = ("Invalid user", falcon.HTTP_400)
    NOT_FOUND_USER = ("Not found user", falcon.HTTP_404)
    FAILED_CREATE_USER = ("Failed create user", falcon.HTTP_500)
    FAILED_READ_USER = ("Failed read user", falcon.HTTP_500)
    FAILED_READ_USERS = ("Failed read users", falcon.HTTP_500)
    FAILED_UPDATE_USER = ("Failed update user", falcon.HTTP_500)
    FAILED_DELETE_USER = ("Failed delete user", falcon.HTTP_500)
    UNEXPECTED_ERROR = ("Unexpected error", falcon.HTTP_500)
    APPLICATION_ID_DEPLICATED = ("Application id is deplicated", falcon.HTTP_500)
    INVALID_APPLICATION = ("Invalid application", falcon.HTTP_400)
    FAILED_CREATE_APPLICATION = ("Failed create application", falcon.HTTP_500)

    def __init__(self, message: str, status: str) -> None:
        self.message = message
        self.status = status
