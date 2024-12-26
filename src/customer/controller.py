from core.security import is_admin
from typing import Annotated
from src.customer.model import CustomerCreate, CustomerUpdate, CustomerPublic
from src.customer.service import Customer as CustomerService
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/customers",
    tags=["customers"],
    responses={404: {"description": "Not found"}},
)

customer_service = CustomerService()


@router.get("/{customer_id}", response_model=CustomerPublic)
async def read_costumer(
    customer_id: int, service: Annotated[CustomerService, Depends(customer_service)]
):
    return service.read(customer_id)


@router.get("/", response_model=list[CustomerPublic])
async def read_all(service: Annotated[CustomerService, Depends(customer_service)]):
    return service.read_all()


@router.post("/", response_model=CustomerPublic)
async def create_customer(
    body: CustomerCreate, service: Annotated[CustomerService, Depends(customer_service)]
):
    return service.create(body)


@router.put("/", response_model=CustomerPublic)
async def update_customer(
    body: CustomerUpdate,
    service: Annotated[CustomerService, Depends(customer_service)],
):
    return service.update(body)


@router.delete("/{customer_id}")
async def delete_costumer(
    customer_id: int,
    service: Annotated[CustomerService, Depends(customer_service)],
    is_admin: bool = Depends(is_admin),
):
    return service.delete(customer_id)
