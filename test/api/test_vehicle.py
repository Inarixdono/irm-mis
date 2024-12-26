from ..helper import vehicle_example
from fastapi.testclient import TestClient


def test_create_vehicle(client: TestClient, headers: dict):
    response = client.post("/vehicles/", headers=headers, json=vehicle_example)
    assert response.status_code == 200
    assert response.json()["vin"] == vehicle_example["vin"]
    assert response.json()["model_id"] == vehicle_example["model_id"]
    assert response.json()["year"] == vehicle_example["year"]
    assert response.json()["color"] == vehicle_example["color"]
    assert response.json()["engine_number"] == vehicle_example["engine_number"]
    assert response.json()["license_plate"] == vehicle_example["license_plate"]
    assert response.json()["price"] == vehicle_example["price"]
    assert response.json()["branch_id"] == vehicle_example["branch_id"]
    assert response.json()["is_new"]
    assert response.json()["inbound_date"]
    assert response.json()["is_active"]
    assert response.json()["created_at"]
    assert response.json()["created_by"] == 1
    assert response.json()["updated_at"] is None
    assert response.json()["updated_by"] is None


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
