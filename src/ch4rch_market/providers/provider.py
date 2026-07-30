# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from abc import abstractmethod

from ch4rch_market.core.modules.base import Module


class Provider(Module):
    """
    Base market data provider.
    """


    @property
    @abstractmethod
    def name(self) -> str:
        ...


    @abstractmethod
    async def connect(self) -> None:
        ...


    @abstractmethod
    async def disconnect(self) -> None:
        ...
