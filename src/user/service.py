from .department import Department
from .model import UserCreate, UserUpdate, User as UserModel
from .role import Role
from src.person.model import Person, PersonCreate
from core.crud import CRUD
from core.security import get_password_hash


class User(CRUD):
    def create(
        self,
        person_create: PersonCreate,
        user_create: UserCreate,
        roles: list[int],
        department_id: int,
    ):
        extra_data = {
            "info": self._get_person(person_create),
            "password": get_password_hash(user_create.password),
            "roles": self._get_roles(roles),
            "department": self._get_department(department_id),
        }
        return super().create(UserModel, user_create, extra_data)

    def update(self, user_update: UserUpdate):
        user_update.password = get_password_hash(user_update.password)
        return super().update(UserModel, user_update)

    def _get_person(self, person_create: PersonCreate) -> Person:
        return Person.model_validate(person_create)

    def __get_role(self, role_id: int) -> Role:
        return super().read(Role, role_id)

    def _get_roles(self, roles: list[int]) -> list[Role]:
        return list(map(self.__get_role, roles))

    def _get_department(self, department_id: int) -> Department:
        return super().read(Department, department_id) if department_id else None
