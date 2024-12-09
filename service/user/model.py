from core.types import ModelUpdate, SQLModel, Audit
from sqlmodel import Field


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
