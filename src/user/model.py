from core.types import Audit, TableModel, PublicModel, UpdateModel
from typing import TYPE_CHECKING
from sqlalchemy import CHAR
from sqlmodel import SQLModel, Field, Relationship


if TYPE_CHECKING:
    from ..branch.model import Branch
    from .department import Department
    from .role import Role


class UserBase(SQLModel):
    name: str = Field(min_length=8, max_length=64, index=True)
    identity_number: str = Field(
        min_length=11, max_length=11, unique=True, sa_type=CHAR(11)
    )
    email: str = Field(min_length=8, max_length=64, unique=True)
    branch_id: int = Field(gt=0, foreign_key="branch.id")
    role_id: int = Field(gt=0, foreign_key="role.id")
    department_id: int = Field(gt=0, foreign_key="department.id")
    note: str | None = Field(default=None, min_length=8, max_length=255)


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=64)


class UserPublic(Audit, UserBase, PublicModel):
    pass


class UserUpdate(UserBase, UpdateModel):
    name: str | None = Field(default=None, min_length=8, max_length=64)
    identity_number: str | None = Field(default=None, min_length=11, max_length=11)
    email: str | None = Field(default=None, min_length=8, max_length=64)
    password: str | None = Field(default=None, min_length=8, max_length=64)
    branch_id: int | None = Field(default=None, gt=0)
    role_id: int | None = Field(default=None, gt=0)
    department_id: int | None = Field(default=None, gt=0)


class User(Audit, UserBase, TableModel, table=True):
    password: str
    branch: "Branch" = Relationship(back_populates="users")
    role: "Role" = Relationship(back_populates="users")
    department: "Department" = Relationship(back_populates="users")
