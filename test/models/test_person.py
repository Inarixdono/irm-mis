from ..helper import person_example
from core.crud import CRUD
from core.config import settings
from src.person.model import Person, PersonCreate, PersonUpdate


def test_first_person(crud: CRUD):
    person: Person = crud.read(Person, 1)
    assert person.name == settings.SUPERUSER_NAME
    assert person.identity_number == settings.SUPERUSER_DOCUMENT_NUMBER
    assert person.is_active
    assert person.created_at is not None
    assert person.updated_at is None


def test_create_person(crud: CRUD):
    person_create = PersonCreate(**person_example)
    person: Person = crud.create(Person, person_create)
    assert hasattr(person, "id")
    assert person.name == person_example["name"]
    assert person.identity_number == person_example["identity_number"]
    assert person.is_active
    assert person.created_at is not None
    assert person.updated_at is None


def test_update_person(crud: CRUD):
    person_to_update: Person = crud.read(Person, 2)
    person_to_update.name = "SUGURU GETO"
    person_to_update.identity_number = "45856988521"
    updated_person: Person = crud.update(
        Person,
        PersonUpdate(
            id=person_to_update.id,
            name=person_to_update.name,
            identity_number=person_to_update.identity_number,
        ),
    )
    assert updated_person.name == person_to_update.name
    assert updated_person.identity_number == person_to_update.identity_number
    assert updated_person.created_at == person_to_update.created_at
    assert updated_person.updated_at is not None


def test_total_persons(crud: CRUD):
    total_persons = crud.read_all(Person)
    assert len(total_persons) == 2
