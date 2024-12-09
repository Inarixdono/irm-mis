import os
from passlib.context import CryptContext


class Config:
    DATABASE_DEVELOPMENT = os.getenv("DATABASE_DEVELOPMENT")
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



settings = Config()
