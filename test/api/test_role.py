from fastapi.testclient import TestClient
from core.types import Role


def test_first_role(client: TestClient, headers: dict):
    response = client.get("/roles/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == Role.SUPERUSER


def test_create_role(client: TestClient, headers: dict):
    response = client.post("/roles/", json={"name": "new_role"}, headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == "new_role"


def test_update_role(client: TestClient, headers: dict):
    response = client.put(
        "/roles/", json={"id": 2, "name": "new_role_updated"}, headers=headers
    )
    assert response.status_code == 200
    assert response.json()["name"] == "new_role_updated"
