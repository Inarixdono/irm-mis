from .model import UserCreate, UserUpdate, UserPublic, User
from .service import User as UserService
from src.person.model import PersonCreate, PersonUpdate
from typing import Annotated
from fastapi import APIRouter, Depends, Body
from sqlmodel import SQLModel

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


class CreateUserBody(SQLModel):
    info: PersonCreate
    user: UserCreate
    roles: list[Annotated[int, Body(gt=0)]]
    department_id: Annotated[int, Body(gt=0)] = None


class UpdateUserBody(SQLModel):
    user: UserUpdate
    info: PersonUpdate | None = None


@router.get("/{user_id}", response_model=UserPublic)
async def read_user(user_id: int, service: Annotated[UserService, Depends()]):
    return service.read(User, user_id)


@router.get("/", response_model=list[UserPublic])
async def read_all(service: Annotated[UserService, Depends()]):
    return service.read_all(User)


@router.post("/", response_model=UserPublic)
async def create_user(
    body: CreateUserBody,
    service: Annotated[UserService, Depends()],
):
    return service.create(body.info, body.user, body.roles, body.department_id)


@router.put("/", response_model=UserPublic)
async def update_user(body: UpdateUserBody, service: Annotated[UserService, Depends()]):
    return service.update(body.user, body.info)
