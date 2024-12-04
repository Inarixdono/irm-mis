from fastapi import APIRouter, Depends
from typing import Annotated
from service.branch.model import BranchCreate, BranchPublic, Branch, BranchUpdate
from service.branch.service import Branch as BranchService

router = APIRouter(
    prefix="/branches",
    tags=["branches"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[BranchPublic])
async def read_branches(service: Annotated[BranchService, Depends()]):
    return service.read_all(Branch)


@router.get("/{id}", response_model=BranchPublic)
async def read_branch(id: int, service: Annotated[BranchService, Depends()]):
    return service.read(Branch, id)


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
