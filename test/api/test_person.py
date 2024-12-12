from fastapi.testclient import TestClient
from ..helper import person_example, create_person


def test_create_person(client: TestClient):
    response = create_person(client)
    assert response.status_code == 200


def test_read_person(client: TestClient):
    response = client.get("/persons/1")
    assert response.status_code == 200
    assert response.json()["name"] == person_example["name"]


def test_read_all_persons(client: TestClient):
    response = client.get("/persons/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_update_person(client: TestClient):
    person_example["id"] = 1
    person_example["name"] = "SUGURU GETO"
    response = client.put("/persons/", json=person_example)
    assert response.status_code == 200
    assert response.json()["name"] == person_example["name"]
