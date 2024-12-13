from ..helper import user_example, create_user
from core.config import settings
from fastapi.testclient import TestClient


def test_first_user(client: TestClient):
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["email"] == settings.SUPERUSER_EMAIL


def test_create_user(client: TestClient):
    response = create_user(client)
    assert response.status_code == 200
    assert response.json()["email"] == user_example["email"]


def test_read_all_users(client: TestClient):
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_update_user(client: TestClient):
    user_example["id"] = 2
    user_example["email"] = "getosuguru@spiritmanipulation.com"
    response = client.put("/users/", json=user_example)
    assert response.status_code == 200
    assert response.json()["email"] == user_example["email"]
