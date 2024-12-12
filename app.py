from fastapi import FastAPI
from core.database import init_db
from api import api_router

from sqlalchemy.exc import IntegrityError

from core.error_handler import integrity_error_handler

app = FastAPI(lifespan=init_db)

app.include_router(api_router)

app.add_exception_handler(IntegrityError, integrity_error_handler)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health_check")
async def health_check():
    return {"status": "ok"}
