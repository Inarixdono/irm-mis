from core.types import VehicleType


branch_example = {
    "name": "TOKYO",
    "phone_number": "0000000000",
}

customer_example = {
    "name": "SATORU GOJO",
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
    "status": "Available",
    "inbound_date": "2024-12-26T12:41:52.050083",
    "branch_id": 1,
}
