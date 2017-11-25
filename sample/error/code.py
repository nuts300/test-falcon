from enum import Enum, unique
import falcon

@unique
class ErrorCode(Enum):
    INVALID_JSON = ("Invalid json", falcon.HTTP_500)
    INVALID_ID = ("Invalid id", falcon.HTTP_400)
    INVALID_USER = ("Invalid user", falcon.HTTP_400)
    FAILED_CREATE_USER = ("Failed create user", falcon.HTTP_500)
    FAILED_READ_USER = ("Failed read user", falcon.HTTP_500)
    FAILED_READ_USERS = ("Failed read users", falcon.HTTP_500)
    UNEXPECTED_ERROR = ("Unexpected error", falcon.HTTP_500)

    def __init__(self, message: str, status: str):
        self.message = message
        self.status = status
