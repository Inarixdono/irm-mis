from .department import Department
from .model import UserCreate, UserUpdate, User as UserModel
from .role import Role

# from .role import Role
from core.crud import CRUD
from core.config import settings


class User(CRUD):
    def create(self, user_create: UserCreate, roles: list[int], department_id: int):
        user_create.password = self.__hash_password(user_create.password)
        user = UserModel(
            **user_create.model_dump(),
            roles=self._get_roles(roles),
            department=self._get_department(department_id),
        )
        return super().create(UserModel, user)

    def update(self, user_update: UserUpdate):
        user_update.password = self.__hash_password(user_update.password)
        return super().update(UserModel, user_update)

    def __get_role(self, role_id: int):
        return super().read(Role, role_id)

    def _get_roles(self, roles: list[int]):
        return list(map(self.__get_role, roles))

    def _get_department(self, department_id: int):
        return super().read(Department, department_id) if department_id else None

    def __hash_password(self, password: str):
        return settings.pwd_context.hash(password)
