from ..helper import person_example, create_person
from core.config import settings
from fastapi.testclient import TestClient


def test_first_person(client: TestClient):
    response = client.get("/persons/1")
    assert response.status_code == 200
    assert response.json()["name"] == settings.SUPERUSER_NAME


def test_create_person(client: TestClient):
    response = create_person(client)
    assert response.status_code == 200


def test_read_all_persons(client: TestClient):
    response = client.get("/persons/")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_update_person(client: TestClient):
    person_example["id"] = 2
    person_example["name"] = "SUGURU GETO"
    response = client.put("/persons/", json=person_example)
    assert response.status_code == 200
    assert response.json()["name"] == person_example["name"]
