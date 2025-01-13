from core.dependencies import is_admin
from .model import BranchCreate
from .model import BranchUpdate
from .model import BranchPublic
from .service import Branch as BranchService
from typing import Annotated
from fastapi import APIRouter, Depends


router = APIRouter(
    prefix="/branches",
    tags=["branches"],
    responses={404: {"description": "Not found"}},
)

branch_service = BranchService()


@router.get("/{id}", response_model=BranchPublic)
async def read_branch(
    id: int, service: Annotated[BranchService, Depends(branch_service)]
):
    return service.read(id)


@router.get("/", response_model=list[BranchPublic])
async def read_all(service: Annotated[BranchService, Depends(branch_service)]):
    return service.read_all()


@router.post("/", response_model=BranchPublic)
async def create_branch(
    branch: BranchCreate,
    service: Annotated[BranchService, Depends(branch_service)],
    is_admin: bool = Depends(is_admin),
):
    return service.create(branch)


@router.put("/", response_model=BranchPublic)
async def update_branch(
    branch: BranchUpdate,
    service: Annotated[BranchService, Depends(branch_service)],
    is_admin: bool = Depends(is_admin),
):
    return service.update(branch)


@router.delete("/{id}")
async def delete_branch(
    id: int,
    service: Annotated[BranchService, Depends(branch_service)],
    is_admin: bool = Depends(is_admin),
):
    return service.delete(id)
