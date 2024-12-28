from ..helper import assert_creation, vehicle_example
from fastapi.testclient import TestClient


def test_create_vehicle(client: TestClient, headers: dict):
    response = client.post("/vehicles/", headers=headers, json=vehicle_example)
    assert_creation(response, vehicle_example)


def test_read_vechicle(client: TestClient, headers: dict):
    response = client.get("/vehicles/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["vin"] == vehicle_example["vin"]
    assert response.json()["is_active"]


def test_update_vehicle(client: TestClient, headers: dict):
    response = client.put(
        "/vehicles/", headers=headers, json={"id": 1, "price": 2000.00}
    )
    assert response.status_code == 200
    assert response.json()["price"] == 2000.00
    assert response.json()["updated_at"]
    assert response.json()["updated_by"] == 1


def test_delete_vehicle(client: TestClient, headers: dict):
    response = client.delete("/vehicles/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert not response.json()["is_active"]


def test_read_all_vehicles(client: TestClient, headers: dict):
    response = client.get("/vehicles/", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 0
