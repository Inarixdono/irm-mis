from core.crud import CRUD
from core.types import Audit, TableModel, PublicModel, UpdateModel
from core.security import is_admin
from typing import TYPE_CHECKING, Annotated
from fastapi import APIRouter, Depends
from sqlmodel import SQLModel, Field, Relationship


router = APIRouter(
    prefix="/roles",
    tags=["roles"],
    dependencies=[Depends(is_admin)],
    responses={404: {"description": "Not found"}},
)

if TYPE_CHECKING:
    from .model import User


class RoleBase(SQLModel):
    name: str = Field(min_length=4, max_length=64, unique=True)
    description: str | None = Field(default=None, min_length=8, max_length=255)


class RoleCreate(RoleBase):
    pass


class RolePublic(Audit, RoleBase, PublicModel):
    pass


class RoleUpdate(RoleBase, UpdateModel):
    name: str | None = Field(default=None, min_length=4, max_length=64)


class Role(Audit, RoleBase, TableModel, table=True):
    users: list["User"] = Relationship(back_populates="role")


role_service = CRUD(Role)


@router.get("/{role_id}", response_model=RolePublic)
async def read_role(role_id: int, service: Annotated[CRUD, Depends(role_service)]):
    return service.read(role_id)


@router.get("/", response_model=list[RolePublic])
async def read_all(service: Annotated[CRUD, Depends(role_service)]):
    return service.read_all()


@router.post("/", response_model=RolePublic)
async def create_role(
    role: RoleCreate, service: Annotated[CRUD, Depends(role_service)]
):
    return service.create(role)


@router.put("/", response_model=RolePublic)
async def update_role(
    role: RoleUpdate, service: Annotated[CRUD, Depends(role_service)]
):
    return service.update(role)
