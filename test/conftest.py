from core.database import engine
from app import app
from collections.abc import Generator
import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session


@pytest.fixture(scope="session", autouse=True)
def db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
        SQLModel.metadata.drop_all(engine)


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c
