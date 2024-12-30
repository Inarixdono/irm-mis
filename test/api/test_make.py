from fastapi.testclient import TestClient

from ..helper import assert_creation, assert_update, make_example


def test_create_make(client: TestClient, headers: dict):
    response = client.post("/vehicles/makes/", json=make_example, headers=headers)
    assert_creation(response, make_example)


def test_read_make(client: TestClient, headers: dict):
    response = client.get("/vehicles/makes/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == make_example["name"]
    assert response.json()["is_active"]
    assert response.json()["created_by"] == 1
    assert response.json()["created_at"] is not None
    assert response.json()["updated_by"] is None
    assert response.json()["updated_at"] is None


def test_read_all_makes(client: TestClient, headers: dict):
    response = client.get("/vehicles/makes/", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_update_make(client: TestClient, headers: dict):
    make_before = client.get("/vehicles/makes/1", headers=headers).json()
    payload = {
        "id": 1,
        "name": "Nissan",
    }
    response = client.put("/vehicles/makes/", json=payload, headers=headers)
    assert_update(make_before, response, ["name"])


def test_delete_make(client: TestClient, headers: dict):
    response = client.delete("/vehicles/makes/1", headers=headers)
    assert response.status_code == 200
    response = client.get("/vehicles/makes/1", headers=headers)
    assert response.status_code == 404
