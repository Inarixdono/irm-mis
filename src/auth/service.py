from datetime import timedelta
from .model import Token
from core.config import settings
from core.database import SessionDependency
from core.exceptions import InvalidUserException
from core.security import create_access_token, verify_password
from src.user import User
from sqlmodel import select


class Auth:
    def __init__(self, session: SessionDependency):
        self.session = session

    def authenticate_user(self, email: str, password: str) -> bool:
        user: User | None = self.__validate_user(email, password)

        if not user:
            raise InvalidUserException()
        token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        token = create_access_token(
            user=user,
            expires=token_expires,
        )

        return Token(access_token=token, token_type="bearer")

    def __validate_user(self, email: str, password: str) -> bool:
        user = self.__get_user(email)
        if not user:
            return False
        if not verify_password(password, user.password):
            raise InvalidUserException()
        return user

    def __get_user(self, email: str) -> User:
        return self.session.exec(select(User).where(User.email == email)).first()
