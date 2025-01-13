from .model import UserCreate, UserUpdate, User as UserModel

from core.crud import CRUD
from security import PasswordHasher


class User(CRUD):
    def __init__(self):
        super().__init__(UserModel)

    def create(
        self,
        user_create: UserCreate,
    ) -> UserModel:
        extra_data = {
            "password": PasswordHasher.get_password_hash(user_create.password),
        }
        return super().create(user_create, extra_data)

    def update(self, user_update: UserUpdate) -> UserModel:
        if user_update.password:
            user_update.password = PasswordHasher.get_password_hash(
                user_update.password
            )

        return super().update(user_update)
