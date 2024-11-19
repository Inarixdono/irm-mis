from sqlmodel import SQLModel, Field
from datetime import date

class IdentificationDocument(SQLModel):
    type: str
    number: str
    
class Address(SQLModel):
    street: str
    city: str
    state: str
    zip_code: str
    country: str
    reference: str

class Person(SQLModel):
    name: str
    surname: str
    birthdate: date
    gender: str
    identification_document: IdentificationDocument
    phone_number: str
    address: str
