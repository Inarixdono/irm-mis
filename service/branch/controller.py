from fastapi import APIRouter, Depends
from typing import Annotated
from service.branch.model import BranchCreate, BranchPublic, Branch, BranchUpdate
from service.branch.service import Branch as BranchService

router = APIRouter(
    prefix="/branches",
    tags=["branches"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{id}", response_model=BranchPublic)
async def read(id: int, service: Annotated[BranchService, Depends()]):
    return service.read(Branch, id)


@router.get("/", response_model=list[BranchPublic])
async def read_branches(service: Annotated[BranchService, Depends()]):
    return service.read_all(Branch)


@router.post("/", response_model=BranchPublic)
async def create(
    branch: BranchCreate, service: Annotated[BranchService, Depends()]
):
    return service.create(Branch, branch)


@router.put("/", response_model=BranchPublic)
async def update(
    branch: BranchUpdate, service: Annotated[BranchService, Depends()]
):
    return service.update(Branch, branch)
