from contextlib import asynccontextmanager
from typing import Annotated
from core.config import settings
from fastapi import Depends, FastAPI
from sqlmodel import Session, create_engine, SQLModel

engine = create_engine(settings.database_development)


@asynccontextmanager
async def init_db(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


async def get_session():
    with Session(engine) as session:
        yield session


SessionDependency = Annotated[Session, Depends(get_session)]
