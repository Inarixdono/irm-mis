from core.config import settings
from core.crud import CRUD
from core.security import get_password_hash
from core.types import Role as RoleEnum, Department as DepartmentEnum
from src.client.model import Client
from src.branch.model import Branch
from src.user.model import User, UserCreate, UserUpdate
from src.user.department import Department
from src.user.role import Role

from ..helper import client_example, user_example


def test_first_branch(crud: CRUD):
    branch: Branch = crud.read(Branch, 1)
    assert branch.name == settings.SUPERUSER_BRANCH


def test_first_role(crud: CRUD):
    role: Role = crud.read(Role, 1)
    assert role.name == RoleEnum.SUPERUSER


def test_first_department(crud: CRUD):
    department: Department = crud.read(Department, 1)
    assert department.name == DepartmentEnum.DEVELOPMENT


def test_create_user(crud: CRUD):
    plain_password = user_example["password"]
    user: User = crud.create(
        User,
        UserCreate(**user_example),
        extra_data={
            "info": Client(**client_example).sqlmodel_update({"created_by": 1}),
            "password": get_password_hash(plain_password),
        },
    )

    assert hasattr(user, "id")
    assert user.info.name == client_example["name"]
    assert user.info.identity_number == client_example["identity_number"]
    assert user.info.created_by == 1
    assert user.info.created_at is not None
    assert user.info.updated_by is None
    assert user.info.updated_at is None

    assert user.email == user_example["email"]
    assert plain_password != user.password
    assert user.branch_id == user_example["branch_id"]
    assert user.is_active
    assert user.created_by == 1
    assert user.created_at is not None
    assert user.updated_by is None
    assert user.updated_at is None


def test_update_user(crud: CRUD):
    user_before: User = crud.read(User, 2).model_copy()
    updated_user: User = crud.update(
        User,
        UserUpdate(
            id=2,
            email="getosuguru@spiritmanipulation.com",
            password=get_password_hash("jureisoujutsuuzumaki"),
        ),
    )

    assert updated_user.id == user_before.id
    assert updated_user.email != user_before.email
    assert updated_user.password != user_before.password
    assert updated_user.created_at == user_before.created_at
    assert updated_user.updated_at is not None


def test_delete_user(crud: CRUD):
    user: User = crud.delete(User, 2)
    assert not user.is_active
    assert user.updated_by == 1
    assert user.updated_at is not None


def test_total_users(crud: CRUD):
    total_users = crud.read_all(User)
    assert len(total_users) == 1
