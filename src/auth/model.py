from sqlmodel import SQLModel


class Token(SQLModel):
    access_token: str
    token_type: str


class TokenData(SQLModel):
    id: int = None
    name: str = None
    email: str = None
    roles: list[str] = []
    department: str = None


class Login(SQLModel):
    email: str
    password: str
