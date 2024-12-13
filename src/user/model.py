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
    id: int
    email: str = Field(max_length=50, unique=True)
    branch_id: int | None = Field(default=None, foreign_key="branch.id")
    note: str | None = None


class UserCreate(UserBase):
    password: str


class UserUpdate(ModelUpdate):
    email: str | None = None
    password: str | None = None
    branch_id: int | None = None
    note: str | None = None


class UserPublic(UserBase):
    pass


class User(Audit, UserBase, table=True):
    id: int | None = Field(default=None, foreign_key="person.id", primary_key=True)
    password: str
    info: "Person" = Relationship(back_populates="user")
    branch: "Branch" = Relationship(back_populates="users")
    department: "Department" = Relationship(
        back_populates="users", link_model=UserDepartmentLink
    )
    roles: list["Role"] = Relationship(back_populates="users", link_model=UserRoleLink)
