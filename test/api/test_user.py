from fastapi.testclient import TestClient
from ..helper import create_user, create_role, create_department, user_example


def test_create_role(client: TestClient):
    response = create_role(client)
    assert response.status_code == 200


def test_create_department(client: TestClient):
    response = create_department(client)
    assert response.status_code == 200


def test_create_user(client: TestClient):
    response = create_user(client)
    assert response.status_code == 200


def test_read_user(client: TestClient):
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["email"] == user_example["email"]


def test_read_all_users(client: TestClient):
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_update_user(client: TestClient):
    user_example["id"] = 1
    user_example["email"] = "getosuguru@spiritmanipulation.com"
    response = client.put("/users/", json=user_example)
    assert response.status_code == 200
    assert response.json()["email"] == user_example["email"]
