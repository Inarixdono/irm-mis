from .model import Customer as CustomerModel, CustomerCreate
from core.crud import CRUD


class Customer(CRUD):
    def __init__(self):
        super().__init__(CustomerModel)

    def create(self, customer_create: CustomerCreate) -> CustomerModel:
        extra_data = {"branch_id": self.current_user.branch_id}
        return super().create(customer_create, extra_data)
