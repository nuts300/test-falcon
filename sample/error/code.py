from enum import Enum, unique

@unique
class ErrorCode(Enum):
    INVALID_JSON = 'Invalid json'
    INVALID_ID = 'Invalid id'
    INVALID_USER = "Invalid user"
    FAILED_CREATE_USER = "Failed create user"
    FAILED_READ_USER = "Failed read user"
    FAILED_READ_USERS = "Failed read users"
    UNEXPECTED_ERROR = "Unexpected error"
