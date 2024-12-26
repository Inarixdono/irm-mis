from .model import Customer as CustomerModel
from core.crud import CRUD


class Customer(CRUD):
    def __init__(self):
        super().__init__(CustomerModel)
