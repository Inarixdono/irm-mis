from core.types import Address, Audit, IdentityType, ModelUpdate
from typing import TYPE_CHECKING
from sqlalchemy import CHAR
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from ..user.model import User


class PersonBase(SQLModel):
    name: str = Field(min_length=5, max_length=128, index=True)
    identity_type: IdentityType = "national_id"
    identity_number: str = Field(min_length=8, max_length=14, unique=True)
    phone_number: str | None = Field(
        default=None, min_length=10, max_length=10, sa_type=CHAR(10)
    )


class PersonCreate(Address, PersonBase):
    pass


class PersonUpdate(Address, PersonBase, ModelUpdate):
    name: str | None = Field(default=None, min_length=5, max_length=128)
    identity_type: IdentityType | None = None
    identity_number: str | None = Field(default=None, min_length=8, max_length=14)


class PersonPublic(PersonBase):
    id: int


class Person(Audit, PersonCreate, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user: "User" = Relationship(back_populates="info")
