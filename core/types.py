from enum import Enum
from sqlmodel import Field
from datetime import datetime


class Model:
    id: int | None = Field(default=None, primary_key=True)


class Address:
    street: str | None = Field(default=None, max_length=100)
    city: str | None = Field(default=None, max_length=100)
    state: str | None = Field(default=None, max_length=100)
    zip_code: str | None = Field(default=None, min_length=5, max_length=5)
    country: str | None = Field(default=None, max_length=100)
    reference: str | None = Field(default=None, max_length=100)


class Audit:
    is_active: bool = True
    created_by: int | None = Field(default=None)
    created_at: datetime = Field(default=datetime.now())
    updated_by: int | None = None
    updated_at: datetime | None = None


class DocumentType(str, Enum):
    national_id = "national_id"
    passport = "passport"
