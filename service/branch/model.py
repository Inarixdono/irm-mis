from core.types import Address, Audit, Model, ModelUpdate, SQLModel


class BranchBase(SQLModel):
    name: str
    phone_number: str


class BranchCreate(Address, BranchBase):
    pass


class BranchUpdate(Address, ModelUpdate):
    name: str | None = None
    phone_number: str | None = None


class BranchPublic(BranchBase):
    id: int


class Branch(Audit, BranchCreate, Model, table=True):
    pass
