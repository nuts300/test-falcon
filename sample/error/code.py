from enum import Enum, unique

@unique
class ErrorCode(Enum):
    INVALID_USER = "Invalid user"
    FAILED_CREATE_USER = "Failed create user"
