from core.config import settings
from src.user.model import User
from contextlib import asynccontextmanager
from typing import Annotated
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session, create_engine, select

connect_args = {"check_same_thread": False}
engine = create_engine(settings.DATABASE_DEVELOPMENT, connect_args=connect_args)


def create_first_user(session: Session):
    from core.types import Role, Department
    from core.security import get_password_hash
    from src.branch.model import Branch

    password_hash = get_password_hash(settings.SUPERUSER_PASSWORD)

    user = User(
        name=settings.SUPERUSER_NAME,
        identity_number=settings.SUPERUSER_DOCUMENT_NUMBER,
        email=settings.SUPERUSER_EMAIL,
        password=password_hash,
        branch=Branch(name=settings.SUPERUSER_BRANCH),
        department=Department.DEVELOPMENT,
        role=Role.SUPERUSER
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
