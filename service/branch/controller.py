from fastapi import APIRouter, Depends
from typing import Annotated
from service.branch.model import BranchIn, BranchOut, Branch
from service.branch.service import Branch as BranchService

router = APIRouter(
    prefix="/branches",
    tags=["branches"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[BranchOut])
async def read_branches(service: Annotated[BranchService, Depends()]):
    return service.read_all(Branch)

@router.get("/{id}", response_model=BranchOut)
async def read_branch(id: int, service: Annotated[BranchService, Depends()]):
    return service.read(Branch, id)

@router.post("/", response_model=BranchOut)
async def create_branch(branch: BranchIn, service: Annotated[BranchService, Depends()]):
    return service.create(Branch, branch)

@router.put("/{id}", response_model=BranchOut)
async def update_branch(id: int, branch: BranchIn, service: Annotated[BranchService, Depends()]):
    return service.update(Branch, branch)