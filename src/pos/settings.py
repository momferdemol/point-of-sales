# pos/settings.py

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    env_name: str = "local"
    api_key: str = "6cfb67f3-6281-4031-b93-ea85db0dce20"  # dummy

    model_config = SettingsConfigDict(env_file=".env")  # overwrite


def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
