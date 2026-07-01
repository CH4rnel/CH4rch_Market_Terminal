# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃


from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict

import yaml


#_Core_Config_Loader

class ConfigError(Exception):
    pass

@dataclass
class AppConfig:
    name: str
    version: str
    environment: str


@dataclass
class ServerConfig:
    host: str
    port: int


@dataclass
class DatabaseConfig:
    type: str
    path: str


@dataclass
class LoggingConfig:
    level: str
    format: str


@dataclass
class CacheConfig:
    enabled: bool
    ttl_seconds: int


@dataclass
class ProviderConfig:
    enabled: bool
    rate_limit: int = 1


@dataclass
class Config:
    app: AppConfig
    server: ServerConfig
    database: DatabaseConfig
    logging: LoggingConfig
    cache: CacheConfig
    providers: Dict[str, ProviderConfig]
    raw: Dict[str, Any]

#_Loader_function

def load_config(path: str = "configs/application.yaml") -> Config:
    config_path = Path(path)

    if not config_path.exists():
        raise ConfigError(f"Config file not found: {path}")

    with config_path.open("r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    try:
        return Config(
            app=AppConfig(**raw["app"]),
            server=ServerConfig(**raw["server"]),
            database=DatabaseConfig(**raw["database"]),
            logging=LoggingConfig(**raw["logging"]),
            cache=CacheConfig(**raw["cache"]),
            providers={
                k: ProviderConfig(**v)
                for k, v in raw["providers"].items()
            },
            raw=raw
        )
    except Exception as e:
        raise ConfigError(f"Invalid configuration structure: {e}")
