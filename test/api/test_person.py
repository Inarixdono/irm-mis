from core.config import settings
from fastapi.testclient import TestClient

from ..helper import person_example


def test_first_person(client: TestClient, headers: dict):
    response = client.get("/persons/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == settings.SUPERUSER_NAME


def test_create_person(client: TestClient, headers: dict):
    response = client.post("/persons/", json=person_example, headers=headers)
    assert response.status_code == 200


def test_read_all_persons(client: TestClient, headers: dict):
    response = client.get("/persons/", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_update_person(client: TestClient, headers: dict):
    person_before = person_example.copy()
    person_to_update = person_example.copy()
    person_to_update["id"] = 2
    person_to_update["name"] = "SUGURU GETO"
    response = client.put("/persons/", json=person_to_update, headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] != person_before["name"]
