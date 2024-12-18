from core.security import get_current_user
from src.person.controller import router as person_router
from src.branch.controller import router as branch_router
from src.user.controller import router as user_router
from src.user.role import router as role_router
from src.user.department import router as department_router
from fastapi import APIRouter, Depends

api_router = APIRouter(dependencies=[Depends(get_current_user)])

api_router.include_router(person_router)
api_router.include_router(branch_router)
api_router.include_router(user_router)
api_router.include_router(role_router)
api_router.include_router(department_router)
