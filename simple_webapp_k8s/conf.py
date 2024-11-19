"""This module contains configuration settings for the application."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuration settings for the application."""

    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        """Configuration settings for the application."""

        env_file = ".env"


settings = Settings()
