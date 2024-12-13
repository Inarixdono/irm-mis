from fastapi import APIRouter, Depends
from typing import Annotated
from src.branch.model import BranchCreate, BranchPublic, Branch, BranchUpdate
from src.branch.service import Branch as BranchService


router = APIRouter(
    prefix="/branches",
    tags=["branches"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{id}", response_model=BranchPublic)
async def read_branch(id: int, service: Annotated[BranchService, Depends()]):
    return service.read(Branch, id)


@router.get("/", response_model=list[BranchPublic])
async def read_all(service: Annotated[BranchService, Depends()]):
    return service.read_all(Branch)


@router.post("/", response_model=BranchPublic)
async def create_branch(
    branch: BranchCreate, service: Annotated[BranchService, Depends()]
):
    return service.create(Branch, branch)


@router.put("/", response_model=BranchPublic)
async def update_branch(
    branch: BranchUpdate, service: Annotated[BranchService, Depends()]
):
    return service.update(Branch, branch)
