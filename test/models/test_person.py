from ..helper import person_example
from service.person.model import PersonCreate, Person
from core.crud import CRUD


def test_create_person(crud: CRUD):
    person = PersonCreate(**person_example)
    person_db: Person = crud.create(Person, person)
    assert hasattr(person_db, "id")
    assert person_db.name == person.name
    assert person_db.created_at is not None
    assert person_db.updated_at is None
