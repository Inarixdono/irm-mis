from core.exceptions import InsufficientPermissionsException
from core.types import Role
from security import JWTManager
from src.auth import TokenData
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
) -> TokenData:
    payload = JWTManager.decode(token)
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
