from fastapi import FastAPI
from core.database import init_db
from service.person.controller import router as person_router
from service.branch.controller import router as branch_router
from service.user.controller import router as user_router
from service.user.role import router as role_router

app = FastAPI(lifespan=init_db)

app.include_router(person_router)
app.include_router(branch_router)
app.include_router(user_router)
app.include_router(role_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health_check")
async def health_check():
    return {"status": "ok"}
