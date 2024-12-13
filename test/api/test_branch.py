from ..helper import branch_example, create_branch
from core.config import settings
from fastapi.testclient import TestClient


def test_first_branch(client: TestClient):
    response = client.get("/branches/1")
    assert response.status_code == 200
    assert response.json()["name"] == settings.SUPERUSER_BRANCH


def test_create_branch(client: TestClient):
    response = create_branch(client)
    assert response.status_code == 200
    assert response.json()["name"] == branch_example["name"]


def test_read_all_branches(client: TestClient):
    response = client.get("/branches/")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_update_branch(client: TestClient):
    branch_example["id"] = 2
    branch_example["name"] = "SHINJUKU"
    response = client.put("/branches/", json=branch_example)
    assert response.status_code == 200
    assert response.json()["name"] == branch_example["name"]
