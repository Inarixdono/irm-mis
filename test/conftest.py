import pytest
from app import app
from core.database import engine, create_first_user
from core.crud import CRUD
from collections.abc import Generator
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session


@pytest.fixture(scope="session", autouse=True)
def session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


@pytest.fixture(scope="module", autouse=True)
def reset_database(session: Session) -> None:
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    create_first_user(session)


@pytest.fixture(scope="module", autouse=True)
def crud(session: Session) -> Generator[CRUD, None, None]:
    with session as session:
        yield CRUD(session)


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c
