from .link import UserRoleLink, UserDepartmentLink
from core.types import ModelUpdate, SQLModel, Audit
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship


if TYPE_CHECKING:
    from ..person.model import Person
    from ..branch.model import Branch
    from .department import Department
    from .role import Role


class UserBase(SQLModel):
    id: int | None = Field(
        default=None, gt=0, primary_key=True, foreign_key="person.id"
    )
    email: str = Field(min_length=8, max_length=64, unique=True)
    branch_id: int | None = Field(default=None, gt=0, foreign_key="branch.id")
    note: str | None = Field(default=None, min_length=8, max_length=255)


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=64)
    branch_id: int = Field(gt=0)


class UserUpdate(UserBase, ModelUpdate):
    email: str | None = Field(default=None, min_length=8, max_length=64)
    password: str | None = Field(default=None, min_length=8, max_length=64)


class UserPublic(Audit, UserBase):
    id: int


class User(Audit, UserBase, table=True):
    password: str
    info: "Person" = Relationship(back_populates="user")
    branch: "Branch" = Relationship(back_populates="users")
    department: "Department" = Relationship(
        back_populates="users", link_model=UserDepartmentLink
    )
    roles: list["Role"] = Relationship(back_populates="users", link_model=UserRoleLink)
