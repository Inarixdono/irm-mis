from typing import Iterable
from fastapi import UploadFile
from .model import CustomerCreate
from .model import Customer as CustomerModel
from core.crud import CRUD
from core.csv_reader import CSVReader


class Customer(CRUD):
    def __init__(self):
        super().__init__(CustomerModel)

    def create(self, customer_create: CustomerCreate) -> CustomerModel:
        extra_data = {"branch_id": self.current_user.branch_id}
        return super().create(customer_create, extra_data)

    def create_all(self, csv: UploadFile) -> list[CustomerModel]:
        customers = self.__extract_customers_from(csv)
        return super().create_all(customers)

    def __extract_customers_from(self, csv: UploadFile) -> Iterable[CustomerModel]:
        csv_reader = CSVReader()
        dataframe = csv_reader.get_content(csv)
        for named_tuple in dataframe:
            yield self.__extract_customer_from(named_tuple)

    def __extract_customer_from(self, named_tuple) -> CustomerModel:
        return CustomerModel(
            id=named_tuple.id,
            name=named_tuple.name,
            identity_number=str(named_tuple.identity_number),
            phone_number=str(named_tuple.phone_number),
            street=named_tuple.street,
            state=named_tuple.state,
            branch_id=self.current_user.branch_id,
        )
