# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum


class ProviderState(str, Enum):
    """
    Provider lifecycle state.
    """

    CREATED = "created"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"


class Provider(ABC):
    """
    Base provider interface.
    """

    name: str = "unknown"

    def __init__(self) -> None:

        self.state = ProviderState.CREATED


    @abstractmethod
    async def start(self) -> None:
        """
        Start provider.
        """
        ...


    @abstractmethod
    async def stop(self) -> None:
        """
        Stop provider.
        """
        ...


    def is_running(self) -> bool:

        return self.state == ProviderState.RUNNING
