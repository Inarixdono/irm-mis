from core.types import Department
from fastapi.testclient import TestClient


def test_first_department(client: TestClient, headers: dict):
    response = client.get("/departments/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == Department.DEVELOPMENT


def test_create_department(client: TestClient, headers: dict):
    response = client.post(
        "/departments/",
        json={"name": "Test Department", "description": "Test Department Description"},
        headers=headers,
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Department"
    assert response.json()["created_by"] == 1
    assert response.json()["created_at"] is not None


def test_update_department(client: TestClient, headers: dict):
    response = client.put(
        "/departments/",
        json={"id": 2, "name": "Test Department Updated"},
        headers=headers,
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Department Updated"
    assert response.json()["updated_by"] == 1
    assert response.json()["updated_at"] is not None
