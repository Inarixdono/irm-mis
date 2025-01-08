from core.database import init_db
from core.error_handler import integrity_error_handler
from src.auth import auth_router
from api import api_router
from fastapi import FastAPI
from sqlalchemy.exc import IntegrityError



app = FastAPI(lifespan=init_db)

app.include_router(auth_router)
app.include_router(api_router)

app.add_exception_handler(IntegrityError, integrity_error_handler)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health_check")
async def health_check():
    return {"status": "ok"}
