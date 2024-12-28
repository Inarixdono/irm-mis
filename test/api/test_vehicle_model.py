from ..helper import assert_creation, model_example
from fastapi.testclient import TestClient


def test_create_model(client: TestClient, headers: dict):
    response = client.post("/vehicles/models/", headers=headers, json=model_example)
    assert_creation(response, model_example)


def test_read_model(client: TestClient, headers: dict):
    response = client.get("/vehicles/models/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == model_example["name"]
    assert response.json()["vehicle_type"] == model_example["vehicle_type"]
    assert response.json()["make_id"] == model_example["make_id"]
    assert response.json()["is_active"]
    assert response.json()["created_by"] == 1
    assert response.json()["created_at"] is not None
    assert response.json()["updated_by"] is None
    assert response.json()["updated_at"] is None


def test_update_model(client: TestClient, headers: dict):
    model_before = client.get("/vehicles/models/1", headers=headers).json()
    response = client.put(
        "/vehicles/models/", headers=headers, json={"id": 1, "name": "LEAD 110"}
    )
    assert response.status_code == 200
    assert response.json()["name"] != model_before["name"]
    assert response.json()["vehicle_type"] == model_before["vehicle_type"]
    assert response.json()["make_id"] == model_before["make_id"]
    assert response.json()["created_by"] == model_before["created_by"]
    assert response.json()["created_at"] == model_before["created_at"]
    assert response.json()["updated_by"] == 1
    assert response.json()["updated_at"] is not None


def test_delete_model(client: TestClient, headers: dict):
    response = client.delete("/vehicles/models/1", headers=headers)
    assert response.status_code == 200
    assert not response.json()["is_active"]


def test_read_all_models(client: TestClient, headers: dict):
    response = client.get("/vehicles/models/", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 0
