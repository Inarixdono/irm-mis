from src.user.controller import router as user_router
from src.user.role import router as role_router
from src.user.department import router as department_router
from src.branch.controller import router as branch_router
from src.client.controller import router as client_controller
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(user_router)
api_router.include_router(role_router)
api_router.include_router(department_router)
api_router.include_router(branch_router)
api_router.include_router(client_controller)
