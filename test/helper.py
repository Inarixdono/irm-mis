from fastapi.testclient import TestClient

branch_example = {
    "name": "TOKYO",
    "phone_number": "0000000000",
}

client_example = {
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


def create_branch(client: TestClient):
    return client.post("/branches/", json=branch_example)


def create_person(client: TestClient):
    return client.post("/persons/", json=client_example)


def create_user(client: TestClient):
    data = {
        "info": client_example,
        "user": user_example,
        "roles": [1],
    }
    return client.post("/users/", json=data)
