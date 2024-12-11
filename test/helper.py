from fastapi.testclient import TestClient

branch_example = {
    "name": "SHINJUKU",
    "phone_number": "0000000000",
}

person_example = {
    "name": "SATORU GOJO",
    "document_type": "national_id",
    "document_number": "40255632169",
}

user_example = {
    "id": 1,
    "email": "gojosatoru@infinitevoid.com",
    "branch_id": 1,
    "password": "hollowtechniquepurple",
}


def create_branch(client: TestClient):
    return client.post("/branches/", json=branch_example)


def create_person(client: TestClient):
    return client.post("/persons/", json=person_example)


def create_role(client: TestClient):
    return client.post("/roles/", json={"name": "ADMIN"})


def create_department(client: TestClient):
    return client.post("/department/", json={"name": "IT"})


def create_user(client: TestClient):
    data = {
        "user": user_example,
        "roles": [1],
        "department": 1,
    }
    return client.post("/users/", json=data)
