from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = ""
    DEBUG: bool = True


settings = Settings()
