from .utils import branch_example
from fastapi.testclient import TestClient


def test_create_branch(client: TestClient):
    response = client.post("/branches/", json=branch_example)
    assert response.status_code == 200


def test_read_branch(client: TestClient):
    response = client.get("/branches/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == branch_example["name"]


def test_read_all_branches(client: TestClient):
    response = client.get("/branches/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_update_branch(client: TestClient):
    branch_example["id"] = 1
    branch_example["name"] = "SHINJUKU"
    response = client.put("/branches/", json=branch_example)
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == branch_example["name"]
