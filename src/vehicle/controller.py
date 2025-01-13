from .model import MakePublic
from .model import MakeCreate
from .model import MakeUpdate
from .model import VehicleModelPublic
from .model import VehicleModelCreate
from .model import VehicleModelUpdate
from .model import VehicleCreate
from .model import VehicleUpdate
from .model import VehiclePublic
from .model import RequestPublic
from .model import RequestCreateBody
from .service import Make as MakeService
from .service import VehicleModel as VehicleModelService
from .service import Vehicle as VehicleService
from .service import Request as RequestService
from core.dependencies import is_admin
from fastapi import APIRouter, Depends


make_router = APIRouter(
    prefix="/makes",
    tags=["makes"],
    responses={404: {"description": "Not found"}},
)

model_router = APIRouter(
    prefix="/models",
    tags=["models"],
    responses={404: {"description": "Not found"}},
)


vehicle_router = APIRouter(
    prefix="/vehicles",
    tags=["vehicles"],
    responses={404: {"description": "Not found"}},
)

request_router = APIRouter(
    prefix="/requests",
    tags=["requests"],
    responses={404: {"description": "Not found"}},
)

make_service = MakeService()
model_service = VehicleModelService()
vehicle_service = VehicleService()
request_service = RequestService()


# Make routes


@make_router.get("/{make_id}", response_model=MakePublic)
async def read_make(make_id: int, service: MakeService = Depends(make_service)):
    return service.read(make_id)


@make_router.get("/", response_model=list[MakePublic])
async def read_all_makes(service: MakeService = Depends(make_service)):
    return service.read_all()


@make_router.post("/", response_model=MakePublic)
async def create_make(
    body: MakeCreate,
    service: MakeService = Depends(make_service),
    is_admin: bool = Depends(is_admin),
):
    return service.create(body)


@make_router.put("/", response_model=MakePublic)
async def update_make(
    body: MakeUpdate,
    service: MakeService = Depends(make_service),
    is_admin: bool = Depends(is_admin),
):
    return service.update(body)


@make_router.delete("/{make_id}")
async def delete_make(
    make_id: int,
    service: MakeService = Depends(make_service),
    is_admin: bool = Depends(is_admin),
):
    return service.delete(make_id)


# Model routes


@model_router.get("/{model_id}", response_model=VehicleModelPublic)
async def read_model(
    model_id: int, service: VehicleModelService = Depends(model_service)
):
    return service.read(model_id)


@model_router.get("/", response_model=list[VehicleModelPublic])
async def read_all_models(service: VehicleModelService = Depends(model_service)):
    return service.read_all()


@model_router.post("/", response_model=VehicleModelPublic)
async def create_model(
    body: VehicleModelCreate,
    service: VehicleModelService = Depends(model_service),
    is_admin: bool = Depends(is_admin),
):
    return service.create(body)


@model_router.put("/", response_model=VehicleModelPublic)
async def update_model(
    body: VehicleModelUpdate,
    service: VehicleModelService = Depends(model_service),
    is_admin: bool = Depends(is_admin),
):
    return service.update(body)


@model_router.delete("/{model_id}")
async def delete_model(
    model_id: int,
    service: VehicleModelService = Depends(model_service),
    is_admin: bool = Depends(is_admin),
):
    return service.delete(model_id)


# Vehicle routes


@vehicle_router.get("/{vehicle_id}", response_model=VehiclePublic)
async def read_vehicle(
    vehicle_id: int, service: VehicleService = Depends(vehicle_service)
):
    return service.read(vehicle_id)


@vehicle_router.get("/", response_model=list[VehiclePublic])
async def read_all_vehicles(service: VehicleService = Depends(vehicle_service)):
    return service.read_all()


@vehicle_router.post("/", response_model=VehiclePublic)
async def create_vehicle(
    body: VehicleCreate,
    service: VehicleService = Depends(vehicle_service),
):
    return service.create(body)


@vehicle_router.put("/", response_model=VehiclePublic)
async def update_vehicle(
    body: VehicleUpdate,
    service: VehicleService = Depends(vehicle_service),
):
    return service.update(body)


@vehicle_router.delete("/{vehicle_id}", response_model=VehiclePublic)
async def delete_vehicle(
    vehicle_id: int,
    service: VehicleService = Depends(vehicle_service),
    is_admin: bool = Depends(is_admin),
):
    return service.delete(vehicle_id)


# Request routes


@request_router.post("/", response_model=RequestPublic)
async def create_request(
    body: RequestCreateBody,
    service: RequestService = Depends(request_service),
):
    return service.create(body)


vehicle_router.include_router(make_router)
vehicle_router.include_router(model_router)
vehicle_router.include_router(request_router)
