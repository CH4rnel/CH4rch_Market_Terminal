# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class Module(ABC):
    """Base class for all runtime modules."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Module name."""
        ...

    @abstractmethod
    async def start(self) -> None:
        """Start module."""
        ...

    @abstractmethod
    async def stop(self) -> None:
        """Stop module."""
        ...
