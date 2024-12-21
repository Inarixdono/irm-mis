from fastapi.testclient import TestClient

branch_example = {
    "name": "TOKYO",
    "phone_number": "0000000000",
}

person_example = {
    "name": "SATORU GOJO",
    "identity_number": "40255632169",
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
    return client.post("/persons/", json=person_example)


def create_user(client: TestClient):
    data = {
        "info": person_example,
        "user": user_example,
        "roles": [1],
    }
    return client.post("/users/", json=data)
