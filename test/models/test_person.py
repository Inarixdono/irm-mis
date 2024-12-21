from ..helper import client_example
from core.crud import CRUD
from core.config import settings
from src.client.model import Client, ClientCreate, ClientUpdate


def test_first_person(crud: CRUD):
    person: Client = crud.read(Client, 1)
    assert person.name == settings.SUPERUSER_NAME
    assert person.identity_number == settings.SUPERUSER_DOCUMENT_NUMBER
    assert person.is_active
    assert person.created_at is not None
    assert person.updated_at is None


def test_create_person(crud: CRUD):
    person_create = ClientCreate(**client_example)
    person: Client = crud.create(Client, person_create)
    assert hasattr(person, "id")
    assert person.name == client_example["name"]
    assert person.identity_number == client_example["identity_number"]
    assert person.is_active
    assert person.created_at is not None
    assert person.updated_at is None


def test_update_person(crud: CRUD):
    person_to_update: Client = crud.read(Client, 2)
    person_to_update.name = "SUGURU GETO"
    person_to_update.identity_number = "45856988521"
    updated_person: Client = crud.update(
        Client,
        ClientUpdate(
            id=person_to_update.id,
            name=person_to_update.name,
            identity_number=person_to_update.identity_number,
        ),
    )
    assert updated_person.name == person_to_update.name
    assert updated_person.identity_number == person_to_update.identity_number
    assert updated_person.created_at == person_to_update.created_at
    assert updated_person.updated_at is not None


def test_delete_person(crud: CRUD):
    person: Client = crud.delete(Client, 2)
    assert not person.is_active
    assert person.updated_at is not None


def test_total_people(crud: CRUD):
    total_people = crud.read_all(Client)
    assert len(total_people) == 1
