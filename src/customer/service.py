from typing import Any
from fastapi import UploadFile
from .model import Customer as CustomerModel, CustomerCreate
from core.crud import CRUD
from core.csv_reader import CSVReader


class Customer(CRUD):
    def __init__(self):
        super().__init__(CustomerModel)

    def create(self, customer_create: CustomerCreate) -> CustomerModel:
        extra_data = {"branch_id": self.current_user.branch_id}
        return super().create(customer_create, extra_data)

    def create_all(self, csv: UploadFile) -> list[CustomerModel]:
        customers_create = self.__extract_customers_from(csv)
        return super().create_all(customers_create)

    def __extract_customers_from(self, csv: UploadFile) -> list[CustomerModel]:
        csv_reader = CSVReader()
        customers = csv_reader.get_content(csv)
        return [self.__extract_customer_from(dict) for dict in customers]

    def __extract_customer_from(self, dictionary: dict[str, Any]) -> CustomerModel:
        return CustomerModel(
            id=dictionary["id"],
            name=dictionary["name"],
            identity_number=str(dictionary["identity_number"]),
            phone_number=str(dictionary["phone_number"]),
            street=dictionary["street"],
            state=dictionary["state"],
            branch_id=self.current_user.branch_id,
        )
