from fastapi import APIRouter, Depends
from typing import Annotated
from model.branch import BranchIn, BranchOut, Branch
from service.branch import Branch as BranchService

router = APIRouter(
    prefix="/branches",
    tags=["branches"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{id}", response_model=BranchOut)
async def read_branch(id: int, service: Annotated[BranchService, Depends()]):
    return service.read(Branch, id)

@router.post("/", response_model=BranchOut)
async def create_branch(branch: BranchIn, service: Annotated[BranchService, Depends()]):
    return service.create(Branch, branch)