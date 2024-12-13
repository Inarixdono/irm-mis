from .link import UserRoleLink
from core.types import ModelUpdate, Audit
from core.crud import CRUD
from typing import TYPE_CHECKING, Annotated
from fastapi import APIRouter, Depends
from sqlmodel import SQLModel, Field, Relationship


router = APIRouter(
    prefix="/roles",
    tags=["roles"],
    responses={404: {"description": "Not found"}},
)

if TYPE_CHECKING:
    from .model import User


class RoleBase(SQLModel):
    name: str
    description: str | None = None


class RoleCreate(RoleBase):
    pass


class RoleUpdate(ModelUpdate):
    name: str | None = None


class RolePublic(RoleBase):
    id: int


class Role(Audit, RoleBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    users: list["User"] = Relationship(back_populates="roles", link_model=UserRoleLink)


@router.get("/{role_id}", response_model=RolePublic)
async def read(role_id: int, service: Annotated[CRUD, Depends()]):
    return service.read(Role, role_id)

@router.get("/", response_model=list[RolePublic])
async def read_all(service: Annotated[CRUD, Depends()]):
    return service.read_all(Role)

@router.post("/", response_model=RolePublic)
async def create(role: RoleCreate, service: Annotated[CRUD, Depends()]):
    return service.create(Role, role)

@router.put("/", response_model=RolePublic)
async def update(role: RoleUpdate, service: Annotated[CRUD, Depends()]):
    return service.update(Role, role)
