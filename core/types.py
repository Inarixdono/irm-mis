from enum import Enum
from datetime import datetime
from sqlmodel import SQLModel, Field


class TableModel(SQLModel):
    id: int | None = Field(default=None, gt=0, primary_key=True)


class PublicModel(SQLModel):
    id: int = Field(gt=0)


class UpdateModel(PublicModel):
    pass


class Address:
    street: str | None = Field(default=None, max_length=128)
    city: str | None = Field(default=None, max_length=128)
    state: str | None = Field(default=None, max_length=128)
    reference: str | None = Field(default=None, max_length=128)


class Audit:
    is_active: bool = True
    created_by: int | None = Field(default=None, gt=0)
    created_at: datetime = Field(default=datetime.now())
    updated_by: int | None = Field(default=None, gt=0)
    updated_at: datetime | None = None


class Auditable(Audit, TableModel):
    pass


class IdentityType(str, Enum):
    NATIONAL_ID = "national_id"
    PASSPORT = "passport"
    RNC = "rnc"


class Role(str, Enum):
    SUPERUSER = "Superuser"
    ADMIN = "Admin"
    GUEST = "Guest"


class Department(str, Enum):
    DEVELOPMENT = "Development"
    ADMINISTRATION = "Administration"
    ACCOUNTING = "Accounting"
    SALES = "Sales"
    RECEIVABLES = "Receivables"
    BILLING = "Billing"
    CUSTOMER_SERVICE = "Customer Service"


class CustomerStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    BLACKLISTED = "Blacklisted"


class VehicleType(str, Enum):
    MOTORCYCLE = "Motorcycle"
    SCOOTER = "Scooter"
    FOUR_WHEELER = "Four Wheeler"


class VehicleStatus(str, Enum):
    AVAILABLE = "Available"
    SOLD = "Sold"
    SETTLED = "Settled"
    SEIZED = "Seized"
    STOLEN = "Stolen"


class RequestStatus(str, Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    PAID = "Paid"
    COMPLETED = "Completed"


class RequestType(str, Enum):
    LICENSE_PLATE = "License Plate"
    ENDORSEMENT = "Endorsement"


class DocumentRequestStatus(str, Enum):
    UNKNOWN = "Unknown"
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    AVAILABLE = "Available"
    DELIVERED = "Delivered"
