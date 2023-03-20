from pydantic import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str = "local"
    DEBUG: bool = True
    SECRET_KEY: str = "t10"
    MYSQL_DATABASE: str = "itinerariosr"
    MYSQL_USER: str = "test"
    MYSQL_PASSWORD: str = "test"
    MYSQL_ROOT_PASSWORD: str = "test"
    DATABASE_URL: str = "mysql://test:test@localhost/itinerarios"


settings = Settings()
