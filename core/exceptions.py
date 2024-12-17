from fastapi import HTTPException
from fastapi import status


class InvalidUserException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect user or password",
        )


class InvalidCredentialsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
