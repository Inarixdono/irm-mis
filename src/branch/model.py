from core.types import Address, Audit, UpdateModel, SQLModel
from typing import TYPE_CHECKING
from sqlalchemy import CHAR
from sqlmodel import Field, Relationship


if TYPE_CHECKING:
    from ..user.model import User


class BranchBase(SQLModel):
    name: str = Field(max_length=128, unique=True)
    phone_number: str | None = Field(
        default=None, unique=True, min_length=10, max_length=10, sa_type=CHAR(10)
    )


class BranchCreate(Address, BranchBase):
    pass


class BranchUpdate(BranchBase, UpdateModel):
    name: str | None = Field(default=None, max_length=128, unique=True)


class BranchPublic(Audit, BranchCreate):
    id: int


class Branch(Audit, BranchCreate, table=True):
    id: int | None = Field(default=None, primary_key=True)
    users: list["User"] = Relationship(back_populates="branch")
