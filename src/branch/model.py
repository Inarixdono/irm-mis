from core.types import Address, Audit, ModelUpdate, SQLModel
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship


if TYPE_CHECKING:
    from ..user.model import User


class BranchBase(SQLModel):
    name: str
    phone_number: str


class BranchCreate(Address, BranchBase):
    pass


class BranchUpdate(Address, ModelUpdate):
    name: str | None = None
    phone_number: str | None = None


class BranchPublic(BranchBase):
    id: int


class Branch(Audit, BranchCreate, table=True):
    id: int | None = Field(default=None, primary_key=True)
    users: list["User"] = Relationship(back_populates="branch")
