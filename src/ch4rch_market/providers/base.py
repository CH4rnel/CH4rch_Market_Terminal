# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from abc import abstractmethod

from ch4rch_market.core.modules.base import Module


class Provider(Module):
    """
    Base interface for market data providers.
    """


    @property
    @abstractmethod
    def name(self) -> str:
        """
        Provider unique name.
        """
        ...


    @abstractmethod
    async def connect(self) -> None:
        """
        Initialize provider connection.
        """
        ...


    @abstractmethod
    async def disconnect(self) -> None:
        """
        Close provider connection.
        """
        ...
