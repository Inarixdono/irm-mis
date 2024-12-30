from core.config import settings
from fastapi.testclient import TestClient

from ..helper import assert_update, branch_example, assert_creation


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
    assert_creation(response, branch_example)


def test_update_branch(client: TestClient, headers: dict):
    branch_before = client.get("/branches/2", headers=headers).json()
    payload = {"id": 2, "name": "SHINJUKU"}
    response = client.put("/branches/", json=payload, headers=headers)
    assert_update(branch_before, response, ["name"])
