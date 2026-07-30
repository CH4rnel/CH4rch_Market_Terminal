# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from enum import Enum
from enum import auto


class RuntimeState(Enum):
    """Application lifecycle states."""

    CREATED = auto()

    INITIALIZING = auto()

    STARTING = auto()

    RUNNING = auto()

    STOPPING = auto()

    STOPPED = auto()

    FAILED = auto()
