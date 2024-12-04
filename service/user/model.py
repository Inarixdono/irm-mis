from sqlmodel import SQLModel, Field
from datetime import datetime

class User(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    person_id: int = Field(foreign_key="person.id")
    email: str = Field(max_length=255, unique=True)
    password: str = Field(max_length=255)
    is_active: bool = True
    # branch
    notes: str | None = Field(default=None)
    created_by: int | None = Field(default=None)
    creation_date: datetime | None = None