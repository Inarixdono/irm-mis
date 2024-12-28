from core.types import VehicleType
from httpx import Response


branch_example = {
    "name": "Tokyo Jujutsu High",
    "phone_number": "0000000000",
    "street": "JUJUTSU TECHNICAL COLLEGE",
    "city": "TOKYO",
    "reference": "TOKYO",
}

customer_example = {
    "name": "SATORU GOJO",
    "identity_type": "national_id",
    "identity_number": "40255632169",
    "phone_number": "0000000000",
    "branch_id": 1,
    "street": "JUJUTSU TECHNICAL COLLEGE",
    "city": "TOKYO",
    "state": "TOKYO",
    "reference": "WHERE FUSHIGURO TOJI STABBED ME",
}

user_example = {
    "name": "SATORU GOJO",
    "identity_number": "40255632169",
    "email": "gojosatoru@infinitevoid.com",
    "branch_id": 1,
    "role_id": 1,
    "department_id": 1,
    "password": "hollowtechniquepurple",
}


make_example = {
    "name": "Honda",
}


model_example = {
    "name": "LEAD 100",
    "vehicle_type": VehicleType.SCOOTER,
    "make_id": 1,
}


vehicle_example = {
    "vin": "JH2JF01U0DK000000",
    "model_id": 1,
    "year": 2013,
    "color": "GRAY",
    "engine_number": "JF01E-0000000",
    "license_plate": "29D-0000",
    "price": 2000,
    "is_new": True,
    "status": "Available",
    "inbound_date": "2024-12-26T12:41:52.050083",
    "owner_id": 1,
    "branch_id": 1,
    "note": "This is a note",
}

request_example = {
    "customer_id": 1,
}


def compare_dicts(dict1: dict, dict2: dict) -> bool:
    return all(dict1[key] == dict2[key] for key in dict1 if key in dict2)


def assert_creation(response: Response, expected: dict):
    expected = expected.copy()
    expected.update(
        {"is_active": True, "created_by": 1, "updated_by": None, "updated_at": None}
    )

    assert response.status_code == 200

    response: dict = response.json()

    assert response["id"] is not None
    assert response["created_at"] is not None
    response.pop("id")
    response.pop("created_at")

    assert compare_dicts(response, expected)
