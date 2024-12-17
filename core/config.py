from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_DEVELOPMENT: str
    DATABASE_PRODUCTION: str
    DATABASE_TEST: str
    CAROLINA_USER: str
    CAROLINA_PASSWORD: str

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 180

    SUPERUSER_EMAIL: str
    SUPERUSER_PASSWORD: str
    SUPERUSER_NAME: str
    SUPERUSER_DOCUMENT_NUMBER: str
    SUPERUSER_BRANCH: str


settings = Settings()
