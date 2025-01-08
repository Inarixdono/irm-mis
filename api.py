from src.user.controller import router as user_router
from src.branch import branch_router
from src.customer.controller import router as customer_controller
from src.vehicle.controller import vehicle_router
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(user_router)
api_router.include_router(branch_router)
api_router.include_router(customer_controller)
api_router.include_router(vehicle_router)
