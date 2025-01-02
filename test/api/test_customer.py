from fastapi.testclient import TestClient

from ..helper import assert_update, customer_example, assert_creation


def test_create(client: TestClient, headers: dict):
    response = client.post("/customers/", json=customer_example, headers=headers)
    expected_customer = customer_example.copy()
    expected_customer.update({"branch_id": 1})
    assert_creation(response, expected_customer)


def test_read_all(client: TestClient, headers: dict):
    response = client.get("/customers/", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_create_all(client: TestClient, headers: dict):
    pass


def test_update(client: TestClient, headers: dict):
    customer_before: dict = client.get("/customers/1", headers=headers).json()
    response = client.put(
        "/customers/", json={"id": 1, "name": "SUGURU GETO"}, headers=headers
    )
    assert_update(customer_before, response, ["name"])
