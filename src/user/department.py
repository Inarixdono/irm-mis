from .link import UserDepartmentLink
from core.types import ModelUpdate, Audit
from core.crud import CRUD
from typing import TYPE_CHECKING, Annotated
from fastapi import APIRouter, Depends
from sqlmodel import SQLModel, Field, Relationship


if TYPE_CHECKING:
    from .model import User

router = APIRouter(
    prefix="/department",
    tags=["department"],
    responses={404: {"description": "Not found"}},
)


class DepartmentBase(SQLModel):
    name: str
    description: str | None = None


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentUpdate(ModelUpdate):
    name: str | None = None
    description: str | None = None


class DepartementPublic(DepartmentBase):
    id: int


class Department(Audit, DepartmentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    users: list["User"] = Relationship(back_populates="department", link_model=UserDepartmentLink)


@router.get("/{department_id}", response_model=DepartementPublic)
async def read(department_id: int, service: Annotated[CRUD, Depends()]):
    return service.read(Department, department_id)


@router.get("/", response_model=list[DepartementPublic])
async def read_all(service: Annotated[CRUD, Depends()]):
    return service.read_all(Department)


@router.post("/", response_model=DepartementPublic)
async def create(department: DepartmentCreate, service: Annotated[CRUD, Depends()]):
    return service.create(Department, department)


@router.put("/", response_model=DepartementPublic)
async def update(department: DepartmentUpdate, service: Annotated[CRUD, Depends()]):
    return service.update(Department, department)
