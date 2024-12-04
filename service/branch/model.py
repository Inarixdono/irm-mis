from core.types import Address, Audit, Model, SQLModel

class BranchBase(SQLModel):
    name: str
    phone_number: str

class BranchCreate(Address, BranchBase):
    pass

class BranchUpdate(BranchCreate, Model):
    pass

class BranchPublic(BranchBase, Model):
    pass
    
class Branch(Audit, BranchCreate, Model, table=True):
    pass