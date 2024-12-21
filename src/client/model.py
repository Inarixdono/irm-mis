from core.types import Address, Audit, IdentityType, ModelUpdate
from sqlalchemy import CHAR
from sqlmodel import SQLModel, Field


class ClientBase(SQLModel):
    name: str = Field(min_length=5, max_length=128, index=True)
    identity_type: IdentityType = IdentityType.NATIONAL_ID
    identity_number: str = Field(min_length=8, max_length=14, unique=True)
    phone_number: str = Field(
        min_length=10, max_length=10, unique=True, sa_type=CHAR(10)
    )
    branch_id: int = Field(foreign_key="branch.id")


class ClientCreate(Address, ClientBase):
    pass


class ClientUpdate(Address, ClientBase, ModelUpdate):
    name: str | None = Field(default=None, min_length=5, max_length=128)
    identity_type: IdentityType | None = None
    identity_number: str | None = Field(default=None, min_length=8, max_length=14)
    phone_number: str | None = Field(default=None, min_length=10, max_length=10)
    branch_id: int | None = None


class ClientPublic(Audit, Address, ClientBase):
    id: int


class Client(Audit, ClientCreate, table=True):
    id: int | None = Field(default=None, primary_key=True)
