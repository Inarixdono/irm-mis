from datetime import date
from sqlmodel import SQLModel, Field
from .types import Address, Audit

class PersonBase(SQLModel):
    name: str = Field(max_length=100)
    surname: str | None = Field(default=None, max_length=100)
    birthdate: date | None = None
    gender: str | None = Field(default=None, max_length=1)
    document_type: str | None = None
    document_number: str | None = Field(default=None, max_length=20, unique=True)
    phone_number: str | None = Field(default=None, max_length=10)

class PersonIn(Audit, Address, PersonBase, SQLModel):
    pass


class Person(PersonIn, table=True):
    id: int | None = Field(default=None, primary_key=True)

class PersonOut(SQLModel):
    id: int
    name: str
