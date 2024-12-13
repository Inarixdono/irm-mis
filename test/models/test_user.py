from core.crud import CRUD
from service.user.model import User
from service.person.model import Person
from service.branch.model import BranchCreate, Branch


def test_create_branch(crud: CRUD):
    branch_create = BranchCreate(
        name="Tokyo",
        phone_number="1234567890",
    )
    branch: Branch = crud.create(Branch, branch_create)

    assert hasattr(branch, "id")
    assert branch.name == branch_create.name


def test_create_user(crud: CRUD):
    user = User(
        info=Person(
            name="ITADORI YUJI",
            document_type="national_id",
            document_number="1234567890",
        ),
        email="yujiitadori@bestblackflasherever.com",
        branch_id=1,
        password="sukunascounter",
    )
    user: User = crud.create(User, user)

    assert hasattr(user, "id")
    assert user.info.name == "ITADORI YUJI"
