from core.types import ModelUpdate, Audit, VehicleStatus
from datetime import datetime
from sqlalchemy import CHAR, DOUBLE
from sqlmodel import SQLModel, Field


class VehicleBase(SQLModel):
    vin: str = Field(max_length=32, unique=True, index=True)
    model_id: int = Field(foreign_key="vehicle_model.id")
    year: int = Field(ge=1900)
    color: str = Field(max_length=32)
    engine_number: str | None = Field(
        default=None, max_length=32, unique=True, index=True
    )
    license_plate: str | None = Field(
        default=None,
        min_length=8,
        max_length=8,
        unique=True,
        index=True,
        sa_type=CHAR(8),
    )
    price: float = Field(ge=0.0, sa_type=DOUBLE)
    status: VehicleStatus = VehicleStatus.AVAILABLE
    is_new: bool = Field(default=True)
    inbound_date: datetime = Field(default=datetime.now())
    owner_id: int | None = Field(default=None, foreign_key="customer.id")
    branch_id: int = Field(foreign_key="branch.id")
    note: str | None = Field(default=None, max_length=255)


class VehicleCreate(VehicleBase):
    pass


class VehicleUpdate(VehicleBase, ModelUpdate):
    vin: str | None = Field(default=None, max_length=32)
    model_id: int | None = None
    year: int | None = None
    color: str | None = Field(default=None, max_length=32)
    engine_number: str | None = Field(default=None, max_length=32)
    license_plate: str | None = Field(default=None, min_length=8, max_length=8)
    price: float | None = None
    status: VehicleStatus | None = None
    is_new: bool | None = None
    inbound_date: datetime | None = None
    branch_id: int | None = None


class VehiclePublic(Audit, VehicleBase):
    id: int


class Vehicle(Audit, VehicleBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
