from .link import UserRoleLink
from core.types import ModelUpdate, SQLModel, Audit
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship

if TYPE_CHECKING:
    from .role import Role


class UserBase(SQLModel):
    data: int = Field(foreign_key="person.id")
    email: str = Field(max_length=50, unique=True)
    branch_id: int = Field(foreign_key="branch.id")
    note: str | None = None


class UserCreate(UserBase):
    password: str


class UserUpdate(ModelUpdate):
    email: str | None = None
    password: str | None = None
    branch_id: int | None = None
    note: str | None = None


class UserPublic(UserBase):
    id: int


class User(Audit, UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str
    roles: list["Role"] = Relationship(back_populates="users", link_model=UserRoleLink)
