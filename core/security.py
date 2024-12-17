from datetime import datetime, timedelta, timezone

import jwt
from core.config import settings
from src.user.model import User
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


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
            "name": user.info.name,
            "email": user.email,
            "roles": [role.name for role in user.roles],
            "department": user.department.name if user.department else None,
            "exp": expire,
        },
        key=settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )
