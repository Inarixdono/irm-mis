from src.user import user_router
from src.branch import branch_router
from src.customer import customer_router
from src.vehicle import vehicle_router
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(user_router)
api_router.include_router(branch_router)
api_router.include_router(customer_router)
api_router.include_router(vehicle_router)
