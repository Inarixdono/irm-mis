from .department import Department
from .model import UserCreate, UserUpdate, User as UserModel
from .role import Role

from core.crud import CRUD
from core.security import get_password_hash
from src.person.model import Person, PersonCreate, PersonUpdate


class User(CRUD):
    def create(
        self,
        person_create: PersonCreate,
        user_create: UserCreate,
        roles: list[int],
        department_id: int,
    ) -> UserModel:
        extra_data = {
            "info": self.__create_person(person_create),
            "password": get_password_hash(user_create.password),
            "roles": self._get_roles(roles),
            "department": self._get_department(department_id),
        }
        return super().create(UserModel, user_create, extra_data)

    def update(self, user_update: UserUpdate, person_update: PersonUpdate) -> UserModel:
        payload = {}

        if user_update.password:
            payload["password"] = get_password_hash(user_update.password)

        if person_update:
            payload["info"] = self.__update_person(person_update)

        return super().update(UserModel, user_update)

    def __update_person(self, person_update: PersonUpdate) -> Person:
        update_data = person_update.model_dump(exclude_unset=True)
        return super().read(Person, person_update.id).sqlmodel_update(update_data)

    def __create_person(self, person_create: PersonCreate) -> Person:
        return Person.model_validate(
            person_create, update={"created_by": self.current_user.id}
        )

    def __get_role(self, role_id: int) -> Role:
        return super().read(Role, role_id)

    def _get_roles(self, roles: list[int]) -> list[Role]:
        return list(map(self.__get_role, roles))

    def _get_department(self, department_id: int) -> Department:
        return super().read(Department, department_id) if department_id else None
