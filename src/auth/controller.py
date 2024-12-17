from .model import Token
from .service import Auth as AuthService
from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    prefix="/login",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=Token)
async def login(
    credentials: Annotated[OAuth2PasswordRequestForm, Depends()],
    service: Annotated[AuthService, Depends()],
):
    return service.authenticate_user(credentials.username, credentials.password)
