from .model import Token, Login
from .service import Auth as AuthService
from typing import Annotated
from fastapi import APIRouter, Body, Depends

router = APIRouter(
    prefix="/login",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=Token)
async def login(
    credentials: Annotated[Login, Body()], service: Annotated[AuthService, Depends()]
):
    return service.authenticate_user(credentials.email, credentials.password)
