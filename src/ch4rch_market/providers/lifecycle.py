# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from enum import Enum


class ProviderState(str, Enum):

    CREATED = "created"

    INITIALIZING = "initializing"

    CONNECTING = "connecting"

    CONNECTED = "connected"

    RUNNING = "running"

    STOPPING = "stopping"

    STOPPED = "stopped"

    FAILED = "failed"
