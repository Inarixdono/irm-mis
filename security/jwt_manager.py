import jwt
from core.config import settings
from core.exceptions import InvalidCredentialsException
from typing import TYPE_CHECKING
from datetime import datetime
from datetime import timedelta
from datetime import timezone

if TYPE_CHECKING:
    from src.auth import TokenData
    from src.user import User


class JWTManager:
    __ALGORITHM = "HS256"

    @classmethod
    def create_token(cls, user: "User", expires: timedelta | None = None) -> str:
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
            algorithm=cls.__ALGORITHM,
        )

    @classmethod
    def decode(cls, token: str) -> "TokenData":
        try:
            return jwt.decode(token, settings.SECRET_KEY, algorithms=[cls.__ALGORITHM])
        except jwt.InvalidTokenError:
            raise InvalidCredentialsException()
