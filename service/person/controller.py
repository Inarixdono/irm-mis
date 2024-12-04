from typing import Annotated
from service.person.model import PersonCreate, PersonPublic, Person
from service.person.service import Person as PersonService
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/persons",
    tags=["persons"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=PersonPublic)
async def create_person(
    person: PersonCreate, service: Annotated[PersonService, Depends()]
):
    return service.create(Person, person)
