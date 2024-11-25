from sqlmodel import SQLModel, Field
from datetime import datetime

class Address(SQLModel):
    street: str | None = Field(default=None, max_length=100)
    city: str | None = Field(default=None, max_length=100)
    state: str | None = Field(default=None, max_length=100)
    zip_code: str | None = Field(default=None, min_length=5, max_length=5)
    country: str | None = Field(default=None, max_length=100)
    reference: str | None = Field(default=None, max_length=100)
    
class Audit(SQLModel):
    is_active: bool = True
    created_by: int | None = Field(default=None)
    created_at: datetime = Field(default=datetime.now())
    updated_by: int | None = None
    updated_at: datetime | None = None
