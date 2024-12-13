from typing import Annotated
from src.person.model import PersonCreate, PersonUpdate, PersonPublic, Person
from src.person.service import Person as PersonService
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/persons",
    tags=["persons"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{person_id}", response_model=PersonPublic)
async def get_person(person_id: int, service: Annotated[PersonService, Depends()]):
    return service.read(Person, person_id)


@router.get("/", response_model=list[PersonPublic])
async def get_persons(service: Annotated[PersonService, Depends()]):
    return service.read_all(Person)


@router.post("/", response_model=PersonPublic)
async def create_person(
    person: PersonCreate, service: Annotated[PersonService, Depends()]
):
    return service.create(Person, person)


@router.put("/", response_model=PersonPublic)
async def update_person(
    person: PersonUpdate,
    service: Annotated[PersonService, Depends()],
):
    return service.update(Person, person)
