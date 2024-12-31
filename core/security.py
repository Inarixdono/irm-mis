import jwt
from datetime import datetime, timedelta, timezone
from core.config import settings
from core.exceptions import (
    InsufficientPermissionsException,
    InvalidCredentialsException,
)
from core.types import Role
from src.auth.model import TokenData
from src.user.model import User
from typing import Annotated
from passlib.context import CryptContext
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def create_access_token(user: User, expires: timedelta | None = None):
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


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
) -> TokenData:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
    except jwt.InvalidTokenError:
        raise InvalidCredentialsException()
    return TokenData(
        id=payload.get("id"),
        name=payload.get("name"),
        email=payload.get("email"),
        role=payload.get("role"),
        department=payload.get("department"),
        branch_id=payload.get("branch_id"),
    )


def is_superuser(user: Annotated[TokenData, Depends(get_current_user)]):
    if user.role != Role.SUPERUSER:
        raise InsufficientPermissionsException()
    return True


def is_admin(user: Annotated[TokenData, Depends(get_current_user)]):
    if user.role not in [Role.SUPERUSER, Role.ADMIN]:
        raise InsufficientPermissionsException()
    return True
