from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = ""
    DEBUG: bool = True
    SECRET_KEY: str = "t10"


settings = Settings()
