from core.crud import CRUD
from core.types import Audit, TableModel, PublicModel, UpdateModel
from core.security import is_admin
from fastapi import APIRouter, Depends
from sqlmodel import SQLModel, Field


router = APIRouter(
    prefix="/makes",
    tags=["makes"],
    responses={404: {"description": "Not found"}},
)


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


class MakeService(CRUD):
    def __init__(self):
        super().__init__(Make)


make_service = MakeService()


@router.get("/{make_id}", response_model=MakePublic)
async def read_make(make_id: int, service: MakeService = Depends(make_service)):
    return service.read(make_id)


@router.get("/", response_model=list[MakePublic])
async def read_all(service: MakeService = Depends(make_service)):
    return service.read_all()


@router.post("/", response_model=MakePublic)
async def create_make(
    body: MakeCreate,
    service: MakeService = Depends(make_service),
    is_admin: bool = Depends(is_admin),
):
    return service.create(body)


@router.put("/", response_model=MakePublic)
async def update_make(
    body: MakeUpdate,
    service: MakeService = Depends(make_service),
    is_admin: bool = Depends(is_admin),
):
    return service.update(body)


@router.delete("/{make_id}")
async def delete_make(
    make_id: int,
    service: MakeService = Depends(make_service),
    is_admin: bool = Depends(is_admin),
):
    return service.delete(make_id)
