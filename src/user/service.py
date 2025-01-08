from .model import UserCreate
from .model import UserUpdate
from .model import User as UserModel
from core.crud import CRUD
from core.security import get_password_hash


class User(CRUD):
    def __init__(self):
        super().__init__(UserModel)

    def create(
        self,
        user_create: UserCreate,
    ) -> UserModel:
        extra_data = {
            "password": get_password_hash(user_create.password),
        }
        return super().create(user_create, extra_data)

    def update(self, user_update: UserUpdate) -> UserModel:
        if user_update.password:
            user_update.password = get_password_hash(user_update.password)

        return super().update(user_update)
