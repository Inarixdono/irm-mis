from sqlmodel import SQLModel, Field
from core.types import Address, Audit, DocumentType, ModelUpdate


class PersonBase(SQLModel):
    name: str = Field(max_length=100)
    document_type: DocumentType
    document_number: str = Field(max_length=20, unique=True)
    phone_number: str | None = Field(default=None, max_length=10)


class PersonCreate(Address, PersonBase):
    pass


class PersonUpdate(ModelUpdate):
    name: str | None = None
    document_type: DocumentType | None = None
    document_number: str | None = None
    phone_number: str | None = None


class PersonPublic(PersonBase):
    id: int


class Person(Audit, PersonCreate, table=True):
    id: int | None = Field(default=None, primary_key=True)
