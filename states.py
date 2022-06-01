from enum import Enum, auto


class LoginState(Enum):
    USER_NOT_FOUND = auto()
    INCORRECT_PASSWORD = auto()
    LOGIN_SUCCESSFUL = auto()


class SignupState(Enum):
    EMAIL_ALREADY_EXIST = auto()
    NAME_ALREADY_EXIST = auto()
    SIGNUP_SUCCESSFUL = auto()


class DoneeInsertionState(Enum):
    DONEE_EXISTS = auto()
    INSERTION_SUCCESSFUL = auto()


class PostState(Enum):
    DOESNT_EXIST = auto()
    SUCCESSFUL = auto()


class DonationInsertionState(Enum):
    USER_DOESNT_EXIST = auto()
    DONEE_DOESNT_EXIST = auto()
    INSERTION_SUCCESSFUL = auto()
