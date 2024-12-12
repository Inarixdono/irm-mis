from fastapi import APIRouter

from service.person.controller import router as person_router
from service.branch.controller import router as branch_router
from service.user.controller import router as user_router
from service.user.role import router as role_router
from service.user.department import router as department_router

api_router = APIRouter()

api_router.include_router(person_router)
api_router.include_router(branch_router)
api_router.include_router(user_router)
api_router.include_router(role_router)
api_router.include_router(department_router)
