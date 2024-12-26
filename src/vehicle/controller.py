from .model import VehicleCreate, VehicleUpdate, VehiclePublic
from .make import router as make_router
from .vehicle_model import router as vehicle_model_router
from .service import Vehicle as VehicleService
from core.security import is_admin
from fastapi import APIRouter, Depends


router = APIRouter(
    prefix="/vehicles",
    tags=["vehicles"],
    responses={404: {"description": "Not found"}},
)

router.include_router(make_router)
router.include_router(vehicle_model_router)


vehicle_service = VehicleService()


@router.get("/{vehicle_id}", response_model=VehiclePublic)
async def read_vehicle(
    vehicle_id: int, service: VehicleService = Depends(vehicle_service)
):
    return service.read(vehicle_id)


@router.get("/", response_model=list[VehiclePublic])
async def read_all(service: VehicleService = Depends(vehicle_service)):
    return service.read_all()


@router.post("/", response_model=VehiclePublic)
async def create_vehicle(
    body: VehicleCreate,
    service: VehicleService = Depends(vehicle_service),
):
    return service.create(body)


@router.put("/", response_model=VehiclePublic)
async def update_vehicle(
    body: VehicleUpdate,
    service: VehicleService = Depends(vehicle_service),
):
    return service.update(body)


@router.delete("/{vehicle_id}", response_model=VehiclePublic)
async def delete_vehicle(
    vehicle_id: int,
    service: VehicleService = Depends(vehicle_service),
    is_admin: bool = Depends(is_admin),
):
    return service.delete(vehicle_id)
