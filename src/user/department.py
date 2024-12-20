from .link import UserDepartmentLink
from core.types import ModelUpdate, Audit
from core.crud import CRUD
from typing import TYPE_CHECKING, Annotated
from fastapi import APIRouter, Depends
from sqlmodel import SQLModel, Field, Relationship


if TYPE_CHECKING:
    from .model import User

router = APIRouter(
    prefix="/departments",
    tags=["departments"],
    responses={404: {"description": "Not found"}},
)


class DepartmentBase(SQLModel):
    name: str = Field(min_length=4, max_length=64, unique=True)
    description: str | None = Field(default=None, min_length=8, max_length=255)


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentUpdate(DepartmentBase, ModelUpdate):
    name: str | None = Field(default=None, max_length=64)


class DepartementPublic(Audit, DepartmentBase):
    id: int


class Department(Audit, DepartmentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    users: list["User"] = Relationship(
        back_populates="department", link_model=UserDepartmentLink
    )


department_service = CRUD(Department)


@router.get("/{department_id}", response_model=DepartementPublic)
async def read_department(
    department_id: int, service: Annotated[CRUD, Depends(department_service)]
):
    return service.read(department_id)


@router.get("/", response_model=list[DepartementPublic])
async def read_all(service: Annotated[CRUD, Depends(department_service)]):
    return service.read_all()


@router.post("/", response_model=DepartementPublic)
async def create_department(
    department: DepartmentCreate, service: Annotated[CRUD, Depends(department_service)]
):
    return service.create(department)


@router.put("/", response_model=DepartementPublic)
async def update_department(
    department: DepartmentUpdate, service: Annotated[CRUD, Depends(department_service)]
):
    return service.update(department)
