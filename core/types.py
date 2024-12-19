from enum import Enum
from datetime import datetime
from sqlmodel import SQLModel, Field


class ModelUpdate(SQLModel):
    id: int = Field(gt=0)


class Address:
    street: str | None = Field(default=None, max_length=128)
    city: str | None = Field(default=None, max_length=128)
    state: str | None = Field(default=None, max_length=128)
    reference: str | None = Field(default=None, max_length=128)


class Audit:
    is_active: bool = True
    created_by: int | None = Field(default=None)
    created_at: datetime = Field(default=datetime.now())
    updated_by: int | None = None
    updated_at: datetime | None = None


class IdentityType(str, Enum):
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
