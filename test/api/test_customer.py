from fastapi.testclient import TestClient

from ..helper import customer_example


def test_create_customer(client: TestClient, headers: dict):
    response = client.post("/customers/", json=customer_example, headers=headers)
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["name"] == customer_example["name"]
    assert response.json()["identity_number"] == customer_example["identity_number"]
    assert response.json()["phone_number"] == customer_example["phone_number"]
    assert response.json()["street"] == customer_example["street"]
    assert response.json()["city"] == customer_example["city"]
    assert response.json()["state"] == customer_example["state"]
    assert response.json()["reference"] == customer_example["reference"]
    assert response.json()["created_by"] == 1
    assert response.json()["created_at"] is not None
    assert response.json()["updated_by"] is None
    assert response.json()["updated_at"] is None


def test_read_all_customers(client: TestClient, headers: dict):
    response = client.get("/customers/", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_update_customer(client: TestClient, headers: dict):
    customer_before: dict = client.get("/customers/1", headers=headers).json()
    customer_to_update = customer_before.copy()
    customer_to_update["name"] = "SUGURU GETO"
    response = client.put("/customers/", json=customer_to_update, headers=headers)
    customer_after: dict = client.get("/customers/1", headers=headers).json()
    assert response.status_code == 200
    assert customer_before["name"] != customer_after["name"]
    assert customer_before["street"] == customer_after["street"]
    assert customer_before["created_by"] == customer_after["created_by"]
    assert customer_before["created_at"] == customer_after["created_at"]
    assert customer_before["updated_by"] != customer_after["updated_by"]
    assert customer_before["updated_at"] != customer_after["updated_at"]
