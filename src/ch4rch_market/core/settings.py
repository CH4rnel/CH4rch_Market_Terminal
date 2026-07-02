# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃


# Application settings and configuration management.


from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_ROOT = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    """
    Global application settings.

    Supports:
    - environment variables
    - default values
    """

    app_name: str = Field(
        default="CH4rch Market Terminal",
    )

    version: str = Field(
        default="0.1.0",
    )

    config_dir: Path = Field(
        default=PROJECT_ROOT / "configs",
    )

    logs_dir: Path = Field(
        default=PROJECT_ROOT / "logs",
    )

    model_config = SettingsConfigDict(
        env_prefix="CH4RCH_",
        extra="ignore",
    )
