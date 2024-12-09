from core.crud import CRUD
from core.config import settings
from .model import UserCreate, UserUpdate, User as UserModel


class User(CRUD):
    def create(self, user: UserCreate):
        user.password = self.__hash_password(user.password)
        return super().create(UserModel, user)
    
    def update(self, user: UserUpdate):
        user.password = self.__hash_password(user.password)
        return super().update(UserModel, user)

    def __hash_password(self, password: str):
        return settings.pwd_context.hash(password)
