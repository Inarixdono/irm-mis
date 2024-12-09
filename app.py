from fastapi import FastAPI
from core.database import init_db
from service.person import controller as PersonController
from service.branch import controller as BranchController
from service.user import controller as UserController
from service.user.role import router as role_router

app = FastAPI(lifespan=init_db)

app.include_router(PersonController.router)
app.include_router(BranchController.router)
app.include_router(UserController.router)
app.include_router(role_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health_check")
async def health_check():
    return {"status": "ok"}
