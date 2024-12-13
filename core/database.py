from core.config import settings
from src.user.model import User
from contextlib import asynccontextmanager
from typing import Annotated
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session, create_engine, select

engine = create_engine(settings.DATABASE_DEVELOPMENT)


def create_first_user(session: Session):
    from core.types import DocumentType
    from src.person.model import Person
    from src.branch.model import Branch
    from src.user.department import Department
    from src.user.role import Role

    user = User(
        info=Person(
            name=settings.SUPERUSER_NAME,
            document_type=DocumentType.national_id,
            document_number=settings.SUPERUSER_DOCUMENT_NUMBER,
        ),
        email=settings.SUPERUSER_EMAIL,
        password=settings.SUPERUSER_PASSWORD,
        branch=Branch(name="Puerto Plata", phone_number="809-586-0100"),
        department=Department(name="Development"),
        roles=[Role(name="Superuser")],
    )

    session.add(user)
    session.commit()
    return session.refresh(user)


def init():
    with Session(engine) as session:
        user = session.exec(
            select(User).where(User.email == settings.SUPERUSER_EMAIL)
        ).first()
        if not user:
            create_first_user(session)


@asynccontextmanager
async def init_db(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    init()
    yield


async def get_session():
    with Session(engine) as session:
        yield session


SessionDependency = Annotated[Session, Depends(get_session)]
