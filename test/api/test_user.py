from core.config import settings
from fastapi.testclient import TestClient

from ..helper import assert_creation, user_example


def test_first_user(client: TestClient, headers: dict):
    response = client.get("/users/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["email"] == settings.SUPERUSER_EMAIL


def test_create_user(client: TestClient, headers: dict):
    response = client.post("/users/", json=user_example, headers=headers)
    user_example.pop("password")
    assert_creation(response, user_example)


def test_read_all_users(client: TestClient, headers: dict):
    response = client.get("/users/", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_update_user(client: TestClient, headers: dict):
    user_before = client.get("/users/2", headers=headers).json()
    payload = {
        "id": 2,
        "name": "GETO SUGURU",
        "email": "getosuguru@spiritmanipulation.com",
    }
    response = client.put("/users/", json=payload, headers=headers)
    user_after = response.json()
    assert response.status_code == 200
    assert user_before["email"] != user_after["email"]
    assert user_after["updated_by"] == 1
