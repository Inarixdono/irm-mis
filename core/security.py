import jwt
from core.config import settings
from core.exceptions import InsufficientPermissionsException
from core.exceptions import InvalidCredentialsException
from core.types import Role
from src.auth import TokenData
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
