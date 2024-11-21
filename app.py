from fastapi import FastAPI
from controller import branch, person
from core.database import init_db

app = FastAPI(lifespan=init_db)

app.include_router(person.router)
app.include_router(branch.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health_check")
async def health_check():
    return {"status": "ok"}
