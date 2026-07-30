# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "CH4rch Market Terminal"

    version: str = "0.1.0"

    debug: bool = False

    log_level: str = "INFO"

    database_url: str = "sqlite+aiosqlite:///market.db"


@lru_cache
def get_settings() -> AppSettings:
    return AppSettings()
