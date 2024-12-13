from enum import Enum
from datetime import datetime
from sqlmodel import SQLModel, Field


class ModelUpdate(SQLModel):
    id: int


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


class Document(str, Enum):
    NATIONAL_ID = "national_id"
    PASSPORT = "passport"


class Role(str, Enum):
    SUPERUSER = "Superuser"
    ADMIN = "Admin"
    CLIENT = "Client"
    EMPLOYEE = "Employee"


class Department(str, Enum):
    DEVELOPMENT = "Development"
    ADMINISTRATION = "Administration"
    ACCOUNTING = "Accounting"
    SALES = "Sales"
    CXC = "CXC"
    BILLING = "Billing"
    COSTUMER_SERVICE = "Costumer Service"
