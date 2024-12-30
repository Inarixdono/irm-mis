from fastapi.testclient import TestClient
from core.types import Role

from ..helper import assert_creation, assert_update


def test_first_role(client: TestClient, headers: dict):
    response = client.get("/roles/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == Role.SUPERUSER


def test_create_role(client: TestClient, headers: dict):
    payload = {"name": "new_role"}
    response = client.post("/roles/", json=payload, headers=headers)
    assert_creation(response, payload)


def test_update_role(client: TestClient, headers: dict):
    role_before: dict = client.get("/roles/2", headers=headers).json()
    response = client.put(
        "/roles/", json={"id": 2, "name": "new_role_updated"}, headers=headers
    )
    assert_update(role_before, response, ["name"])
