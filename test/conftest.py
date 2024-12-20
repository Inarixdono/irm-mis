import pytest
from app import app
from core.config import settings
from core.crud import CRUD
from core.security import get_current_user
from src.auth.model import Token, TokenData
from core.database import engine, create_first_user
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


@pytest.fixture(scope="session")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="session", autouse=True)
def token(client: TestClient) -> Token:
    jwt = client.post(
        "/login",
        data={
            "username": settings.SUPERUSER_EMAIL,
            "password": settings.SUPERUSER_PASSWORD,
        },
    )
    return Token(**jwt.json())


@pytest.fixture(scope="session")
def current_user(token: Token) -> TokenData:
    return get_current_user(token.access_token)


@pytest.fixture(scope="session", autouse=True)
def crud(session: Session, current_user: TokenData) -> Generator[CRUD, None, None]:
    crud = CRUD()
    with session as session:
        yield crud(session, current_user)


@pytest.fixture(scope="session", autouse=True)
def headers(token: Token) -> dict:
    return {"Authorization": f"Bearer {token.access_token}"}
