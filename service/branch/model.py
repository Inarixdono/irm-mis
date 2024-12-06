from sqlmodel import Field
from core.types import Address, Audit, ModelUpdate, SQLModel


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
