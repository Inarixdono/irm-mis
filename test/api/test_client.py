from fastapi.testclient import TestClient

from ..helper import client_example


def test_create_client(client: TestClient, headers: dict):
    response = client.post("/clients/", json=client_example, headers=headers)
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["name"] == client_example["name"]
    assert response.json()["identity_number"] == client_example["identity_number"]
    assert response.json()["phone_number"] == client_example["phone_number"]
    assert response.json()["street"] == client_example["street"]
    assert response.json()["city"] == client_example["city"]
    assert response.json()["state"] == client_example["state"]
    assert response.json()["reference"] == client_example["reference"]
    assert response.json()["created_by"] == 1
    assert response.json()["created_at"] is not None
    assert response.json()["updated_by"] is None
    assert response.json()["updated_at"] is None


def test_read_all_clients(client: TestClient, headers: dict):
    response = client.get("/clients/", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_update_client(client: TestClient, headers: dict):
    client_before: dict = client.get("/clients/1", headers=headers).json()
    client_to_update = client_before.copy()
    client_to_update["name"] = "SUGURU GETO"
    response = client.put("/clients/", json=client_to_update, headers=headers)
    client_after: dict = client.get("/clients/1", headers=headers).json()
    assert response.status_code == 200
    assert client_before["name"] != client_after["name"]
    assert client_before["street"] == client_after["street"]
    assert client_before["created_by"] == client_after["created_by"]
    assert client_before["created_at"] == client_after["created_at"]
    assert client_before["updated_by"] != client_after["updated_by"]
    assert client_before["updated_at"] != client_after["updated_at"]
