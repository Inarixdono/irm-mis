from typing import Annotated
from src.client.model import ClientCreate, ClientUpdate, ClientPublic
from src.client.service import Client as PersonService
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/clients",
    tags=["clients"],
    responses={404: {"description": "Not found"}},
)

person_service = PersonService()


@router.get("/{client_id}", response_model=ClientPublic)
async def read_client(
    client_id: int, service: Annotated[PersonService, Depends(person_service)]
):
    return service.read(client_id)


@router.get("/", response_model=list[ClientPublic])
async def read_all(service: Annotated[PersonService, Depends(person_service)]):
    return service.read_all()


@router.post("/", response_model=ClientPublic)
async def create_client(
    body: ClientCreate, service: Annotated[PersonService, Depends(person_service)]
):
    return service.create(body)


@router.put("/", response_model=ClientPublic)
async def update_client(
    body: ClientUpdate,
    service: Annotated[PersonService, Depends(person_service)],
):
    return service.update(body)
