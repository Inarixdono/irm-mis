from core.database import engine
from core.crud import CRUD
from app import app
from collections.abc import Generator
import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="session", autouse=True)
def db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
        SQLModel.metadata.drop_all(engine)


@pytest.fixture(scope="session", autouse=True)
def crud(db: Session) -> Generator[CRUD, None, None]:
    SQLModel.metadata.create_all(engine)
    with db as session:
        yield CRUD(session)
