from datetime import date
from sqlmodel import SQLModel, Field
from core.types import Address, Audit, Model

class PersonBase(SQLModel):
    name: str = Field(max_length=100)
    document_type: str | None = None
    document_number: str | None = Field(default=None, max_length=20, unique=True)
    phone_number: str | None = Field(default=None, max_length=10)

class PersonCreate(Address, PersonBase):
    pass

class PersonUpdate(PersonCreate, Model):
    pass

class PersonPublic(PersonBase, Model):
    pass

class Person(Audit, PersonCreate, Model, table=True):
    pass
