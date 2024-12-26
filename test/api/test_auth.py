from core.config import settings
from core.types import Department, Role
from src.auth.model import Token, TokenData


def test_login(token: Token):
    assert token.access_token
    assert token.token_type == "bearer"


def test_token_decode(current_user: TokenData):
    assert current_user.email == settings.SUPERUSER_EMAIL
    assert current_user.name == settings.SUPERUSER_NAME
    assert current_user.department == Department.DEVELOPMENT
    assert current_user.role == Role.SUPERUSER
