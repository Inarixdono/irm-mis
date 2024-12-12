from fastapi import FastAPI
from core.database import init_db
from api import api_router

app = FastAPI(lifespan=init_db)

app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health_check")
async def health_check():
    return {"status": "ok"}
