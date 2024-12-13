from ..helper import person_example
from src.person.model import Person, PersonCreate, PersonUpdate
from core.crud import CRUD


def test_create_person(crud: CRUD):
    person_create = PersonCreate(**person_example)
    person: Person = crud.create(Person, person_create)
    assert hasattr(person, "id")
    assert person.name == person_create.name
    assert person.created_at is not None
    assert person.updated_at is None

def test_update_person(crud: CRUD):
    person_example["id"] = 1
    person_example["name"] = "SUGURU GETO"
    person_update = PersonUpdate(**person_example)
    person: Person = crud.update(Person, person_update)
    assert person.name == person_update.name
    assert person.updated_at is not None
