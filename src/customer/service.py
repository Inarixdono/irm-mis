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

    async def create_all(self, csv: UploadFile) -> list[CustomerModel]:
        customers_create = await self.__extract_customers_from(csv)
        return super().create_all(customers_create)

    async def __extract_customers_from(self, csv: UploadFile) -> list[CustomerCreate]:
        content = await self.__read_file(csv)
        return list(map(self.__extract_customer_from, content))

    def __read_file(self, csv: UploadFile) -> list[list[str]]:
        csv_reader = CSVReader()
        return csv_reader.get_content(csv)

    def __extract_customer_from(self, line: list[str]) -> CustomerModel:
        return CustomerModel(
            id=line[0],
            name=line[1],
            identity_number=line[2],
            phone_number=line[3],
            street=line[4],
            state=line[5],
            branch_id=self.current_user.branch_id,
        )
