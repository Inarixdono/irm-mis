from fastapi import FastAPI
from core.database import init_db
from service.person import controller as PersonController
from service.branch import controller as BranchController

app = FastAPI(lifespan=init_db)

app.include_router(PersonController.router)
app.include_router(BranchController.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health_check")
async def health_check():
    return {"status": "ok"}


# TODO: Terminar feature de branches
# TODO: Terminar feature de usuario
