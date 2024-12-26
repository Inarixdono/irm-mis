from .model import Vehicle as VehicleModel
from core.crud import CRUD


class Vehicle(CRUD):
    def __init__(self):
        super().__init__(VehicleModel)
