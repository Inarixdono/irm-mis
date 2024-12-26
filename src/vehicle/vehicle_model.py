from core.crud import CRUD
from core.types import Audit, TableModel, PublicModel, UpdateModel, VehicleType
from core.security import is_admin
from fastapi import APIRouter, Depends
from sqlmodel import SQLModel, Field

router = APIRouter(
    prefix="/models",
    tags=["models"],
    responses={404: {"description": "Not found"}},
)


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


class VehicleModelService(CRUD):
    def __init__(self):
        super().__init__(VehicleModel)


model_service = VehicleModelService()


@router.get("/{model_id}", response_model=VehicleModelPublic)
async def read_model(
    model_id: int, service: VehicleModelService = Depends(model_service)
):
    return service.read(model_id)


@router.get("/", response_model=list[VehicleModelPublic])
async def read_all(service: VehicleModelService = Depends(model_service)):
    return service.read_all()


@router.post("/", response_model=VehicleModelPublic)
async def create_model(
    body: VehicleModelCreate,
    service: VehicleModelService = Depends(model_service),
    is_admin: bool = Depends(is_admin),
):
    return service.create(body)


@router.put("/", response_model=VehicleModelPublic)
async def update_model(
    body: VehicleModelUpdate,
    service: VehicleModelService = Depends(model_service),
    is_admin: bool = Depends(is_admin),
):
    return service.update(body)


@router.delete("/{model_id}")
async def delete_model(
    model_id: int,
    service: VehicleModelService = Depends(model_service),
    is_admin: bool = Depends(is_admin),
):
    return service.delete(model_id)
