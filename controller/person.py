from typing import Annotated
from model.person import PersonIn, Person, PersonOut
from service.person import Person as PersonService
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/persons",
    tags=["persons"],
    responses={404: {"description": "Not found"}},
)   
        
@router.post("/", response_model=PersonOut)
async def create_person(person: PersonIn, service: Annotated[PersonService, Depends()]):
    return service.create(Person ,person)
