from core.config import settings
from core.types import Department, Role
from src.auth.model import Token, TokenData


def test_login(token: Token):
    assert token.access_token
    assert token.token_type == "bearer"


def test_token_decode(get_user: TokenData):
    assert get_user.email == settings.SUPERUSER_EMAIL
    assert get_user.name == settings.SUPERUSER_NAME
    assert get_user.department == Department.DEVELOPMENT
    assert Role.SUPERUSER in get_user.roles
