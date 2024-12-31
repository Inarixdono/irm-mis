from core.types import (
    Audit,
    TableModel,
    PublicModel,
    UpdateModel,
    VehicleType,
    VehicleStatus,
    RequestStatus,
    RequestType,
    DocumentRequestStatus,
)

from datetime import datetime
from sqlalchemy import CHAR, DOUBLE
from sqlmodel import SQLModel, Field, Relationship


# Make


class MakeBase(SQLModel):
    name: str = Field(max_length=64, unique=True, index=True)


class MakeCreate(MakeBase):
    pass


class MakePublic(Audit, MakeBase, PublicModel):
    pass


class MakeUpdate(MakeBase, UpdateModel):
    name: str | None = Field(default=None, max_length=64)


class Make(Audit, MakeBase, TableModel, table=True):
    pass


# Vehicle Model


class VehicleModelBase(SQLModel):
    name: str = Field(max_length=64, unique=True, index=True)
    vehicle_type: VehicleType = VehicleType.MOTORCYCLE
    make_id: int = Field(foreign_key="make.id")


class VehicleModelCreate(VehicleModelBase):
    pass


class VehicleModelPublic(Audit, VehicleModelBase, PublicModel):
    pass


class VehicleModelUpdate(VehicleModelBase, UpdateModel):
    name: str | None = Field(default=None, max_length=64)
    vehicle_type: VehicleType | None = None
    make_id: int | None = None


class VehicleModel(Audit, VehicleModelBase, TableModel, table=True):
    __tablename__ = "vehicle_model"


# Vehicle


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
    branch_id: int = Field(gt=0, foreign_key="branch.id")
    note: str | None = Field(default=None, max_length=255)


class VehicleCreate(VehicleBase):
    pass


class VehiclePublic(Audit, VehicleBase, PublicModel):
    pass


class VehicleUpdate(VehicleBase, UpdateModel):
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
    branch_id: int | None = Field(default=None, gt=0)


class Vehicle(Audit, VehicleBase, TableModel, table=True):
    requests: list["VehicleRequest"] = Relationship(back_populates="vehicle")


# Request


class RequestBase(SQLModel):
    customer_id: int = Field(foreign_key="customer.id")
    status: RequestStatus = RequestStatus.PENDING
    note: str | None = Field(default=None, max_length=255)
    completion_date: datetime | None = None


class RequestCreate(SQLModel):
    customer_id: int = Field(foreign_key="customer.id")
    note: str | None = Field(default=None, max_length=255)


class RequestCreateBody(SQLModel):
    request: RequestCreate
    detail: list["VehicleRequestCreate"]


class RequestPublic(Audit, RequestBase, PublicModel):
    pass


class RequestUpdate(RequestBase, UpdateModel):
    client_id: int | None = None
    status: RequestStatus | None = None
    note: str | None = Field(default=None, max_length=255)
    completion_date: datetime | None = None


class Request(Audit, RequestBase, TableModel, table=True):
    detail: list["VehicleRequest"] = Relationship(back_populates="request")


# Vehicle Request


class VehicleRequestCreate(SQLModel):
    vehicle_id: int = Field(foreign_key="vehicle.id")
    request_type: RequestType = Field(primary_key=True)
    note: str | None = Field(default=None, max_length=255)


class VehicleRequest(SQLModel, table=True):
    __tablename__ = "vehicle_request"
    request_id: int | None = Field(
        default=None, primary_key=True, foreign_key="request.id"
    )
    vehicle_id: int = Field(foreign_key="vehicle.id")
    request_type: RequestType = Field(primary_key=True)
    status: DocumentRequestStatus = DocumentRequestStatus.PENDING
    note: str | None = Field(default=None, max_length=255)
    delivery_date: datetime | None = None

    request: "Request" = Relationship(back_populates="detail")
    vehicle: "Vehicle" = Relationship(back_populates="requests")
