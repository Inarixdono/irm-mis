from datetime import timedelta
from .model import Token
from core.config import settings
from core.exceptions import InvalidUserException
from core.security import create_access_token
from src.user.model import User
from src.user.service import User as UserService
from typing import Annotated
from fastapi import Depends


class Auth:
    def __init__(self, service: Annotated[UserService, Depends()]):
        self.service = service

    def authenticate_user(self, email: str, password: str) -> bool:
        user: User | None = self.service.authenticate_user(email, password)

        if not user:
            raise InvalidUserException()
        token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        token = create_access_token(
            user=user,
            expires=token_expires,
        )

        return Token(access_token=token, token_type="bearer")
