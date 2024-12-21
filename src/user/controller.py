from .model import UserCreate, UserUpdate, UserPublic
from .service import User as UserService
from typing import Annotated
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

user_service = UserService()


@router.get("/{user_id}", response_model=UserPublic)
async def read_user(
    user_id: int, service: Annotated[UserService, Depends(user_service)]
):
    return service.read(user_id)


@router.get("/", response_model=list[UserPublic])
async def read_all(service: Annotated[UserService, Depends(user_service)]):
    return service.read_all()


@router.post("/", response_model=UserPublic)
async def create_user(
    body: UserCreate,
    service: Annotated[UserService, Depends(user_service)],
):
    return service.create(body)


@router.put("/", response_model=UserPublic)
async def update_user(
    body: UserUpdate, service: Annotated[UserService, Depends(user_service)]
):
    return service.update(body)
