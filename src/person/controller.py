from typing import Annotated
from src.person.model import PersonCreate, PersonUpdate, PersonPublic
from src.person.service import Person as PersonService
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/persons",
    tags=["persons"],
    responses={404: {"description": "Not found"}},
)

person_service = PersonService()


@router.get("/{person_id}", response_model=PersonPublic)
async def read_person(
    person_id: int, service: Annotated[PersonService, Depends(person_service)]
):
    return service.read(person_id)


@router.get("/", response_model=list[PersonPublic])
async def read_all(service: Annotated[PersonService, Depends(person_service)]):
    return service.read_all()


@router.post("/", response_model=PersonPublic)
async def create_person(
    person: PersonCreate, service: Annotated[PersonService, Depends(person_service)]
):
    return service.create(person)


@router.put("/", response_model=PersonPublic)
async def update_person(
    person: PersonUpdate,
    service: Annotated[PersonService, Depends(person_service)],
):
    return service.update(person)
