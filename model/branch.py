from sqlmodel import SQLModel, Field, Relationship
from typing import Annotated
from .types import Address, Audit

class BranchBase(SQLModel):
    name: str
    phone_number: str
    admin_id: int = Field(foreign_key="person.id")

class BranchIn(Audit, Address, BranchBase, SQLModel):
    pass
    
class Branch(BranchIn, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
class BranchOut(BranchBase):
    id: int
