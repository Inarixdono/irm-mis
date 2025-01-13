import jwt
from datetime import datetime, timedelta, timezone
from .model import Token
from core.config import settings
from core.database import SessionDependency
from core.exceptions import InvalidUserException
from security import PasswordHasher
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
        token = self.__create_token(
            user=user,
            expires=token_expires,
        )

        return Token(access_token=token, token_type="bearer")

    def __validate_user(self, email: str, password: str) -> bool:
        user = self.__get_user(email)
        if not user:
            return False
        if not PasswordHasher.verify_password(password, user.password):
            raise InvalidUserException()
        return user

    def __get_user(self, email: str) -> User:
        return self.session.exec(select(User).where(User.email == email)).first()

    def __create_token(self, user: User, expires: timedelta | None = None):
        if expires:
            expire = datetime.now(timezone.utc) + expires
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        return jwt.encode(
            payload={
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "role": user.role,
                "department": user.department,
                "branch_id": user.branch_id,
                "exp": expire,
            },
            key=settings.SECRET_KEY,
            algorithm=settings.ALGORITHM,
        )
