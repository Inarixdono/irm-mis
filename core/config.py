from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_development: str
    database_production: str
    database_test: str
    secret_key: str
    carolina_user: str
    carolina_password: str


settings = Settings()
