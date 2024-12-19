from core.config import settings
from fastapi.testclient import TestClient

from ..helper import branch_example


def test_first_branch(client: TestClient, headers: dict):
    response = client.get("/branches/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == settings.SUPERUSER_BRANCH


def test_read_all_branches(client: TestClient, headers: dict):
    response = client.get("/branches/", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_create_branch(client: TestClient, headers: dict):
    response = client.post("/branches/", json=branch_example, headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == branch_example["name"]


def test_update_branch(client: TestClient, headers: dict):
    branch_before = branch_example.copy()
    branch_to_update = branch_example.copy()
    branch_to_update["id"] = 2
    branch_to_update["name"] = "SHINJUKU"
    response = client.put("/branches/", json=branch_to_update, headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] != branch_before["name"]
