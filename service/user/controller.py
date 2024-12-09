from .model import UserCreate, UserUpdate, UserPublic, User
from .service import User as UserService
from typing import Annotated
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{user_id}", response_model=UserPublic)
async def read(user_id: int, service: Annotated[UserService, Depends()]):
    return service.read(User, user_id)


@router.get("/", response_model=list[UserPublic])
async def read_all(service: Annotated[UserService, Depends()]):
    return service.read_all(User)


@router.post("/", response_model=UserPublic)
async def create(user: UserCreate, service: Annotated[UserService, Depends()]):
    return service.create(user)


@router.put("/", response_model=UserPublic)
async def update(user: UserUpdate, service: Annotated[UserService, Depends()]):
    return service.update(user)
