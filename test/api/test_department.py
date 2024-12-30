from core.types import Department
from fastapi.testclient import TestClient

from ..helper import assert_creation, assert_update


def test_first_department(client: TestClient, headers: dict):
    response = client.get("/departments/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == Department.DEVELOPMENT


def test_create_department(client: TestClient, headers: dict):
    payload = {"name": "Test Department", "description": "Test Department Description"}
    response = client.post(
        "/departments/",
        json=payload,
        headers=headers,
    )
    assert_creation(response, payload)


def test_update_department(client: TestClient, headers: dict):
    department_before = client.get("/departments/2", headers=headers).json()
    response = client.put(
        "/departments/",
        json={"id": 2, "name": "Test Department Updated"},
        headers=headers,
    )
    assert_update(department_before, response, ["name"])
