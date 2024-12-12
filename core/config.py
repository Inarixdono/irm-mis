from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_DEVELOPMENT: str
    DATABASE_PRODUCTION: str
    DATABASE_TEST: str
    SECRET_KEY: str
    CAROLINA_USER: str
    CAROLINA_PASSWORD: str
    SUPERUSER_EMAIL: str
    SUPERUSER_PASSWORD: str
    SUPERUSER_NAME: str
    SUPERUSER_DOCUMENT_NUMBER: str
    


settings = Settings()
