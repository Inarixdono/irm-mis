from fastapi.testclient import TestClient

from ..helper import assert_creation, assert_update, vehicle_example


def test_create_vehicle(client: TestClient, headers: dict):
    response = client.post("/vehicles/", headers=headers, json=vehicle_example)
    expected_vehicle = vehicle_example.copy()
    expected_vehicle.update({"branch_id": 1})
    assert_creation(response, expected_vehicle)


def test_read_vechicle(client: TestClient, headers: dict):
    response = client.get("/vehicles/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["vin"] == vehicle_example["vin"]
    assert response.json()["is_active"]


def test_update_vehicle(client: TestClient, headers: dict):
    vehicle_before: dict = client.get("/vehicles/1", headers=headers).json()
    response = client.put(
        "/vehicles/", headers=headers, json={"id": 1, "price": 1500.00}
    )
    assert_update(vehicle_before, response, ["price"])


def test_delete_vehicle(client: TestClient, headers: dict):
    response = client.delete("/vehicles/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert not response.json()["is_active"]


def test_read_all_vehicles(client: TestClient, headers: dict):
    response = client.get("/vehicles/", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 0
