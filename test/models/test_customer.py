from ..helper import customer_example
from core.crud import CRUD
from src.customer import CustomerCreate
from src.customer import CustomerUpdate
from src.customer import Customer


def test_create_customer(crud: CRUD):
    customer_create = CustomerCreate(**customer_example)
    customer: Customer = crud.create(Customer, customer_create)
    assert hasattr(customer, "id")
    assert customer.name == customer_example["name"]
    assert customer.identity_number == customer_example["identity_number"]
    assert customer.is_active
    assert customer.created_at is not None
    assert customer.updated_at is None


def test_update_customer(crud: CRUD):
    customer_to_update: Customer = crud.read(Customer, 2)
    customer_to_update.name = "SUGURU GETO"
    customer_to_update.identity_number = "45856988521"
    updated_customer: Customer = crud.update(
        Customer,
        CustomerUpdate(
            id=customer_to_update.id,
            name=customer_to_update.name,
            identity_number=customer_to_update.identity_number,
        ),
    )
    assert updated_customer.name == customer_to_update.name
    assert updated_customer.identity_number == customer_to_update.identity_number
    assert updated_customer.created_at == customer_to_update.created_at
    assert updated_customer.updated_at is not None


def test_delete_customer(crud: CRUD):
    customer: Customer = crud.delete(Customer, 2)
    assert not customer.is_active
    assert customer.updated_at is not None


def test_total_customers(crud: CRUD):
    total_customers = crud.read_all(Customer)
    assert len(total_customers) == 1
