# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from abc import ABC, abstractmethod

from ch4rch_market.core.event_bus import EventBus


class MarketProvider(ABC):
    """
    Base interface for market data providers.
    """

    name: str = "unknown"

    def __init__(
        self,
        event_bus: EventBus,
    ) -> None:

        self.event_bus = event_bus

        self.running = False


    @abstractmethod
    async def start(self) -> None:
        """
        Initialize provider.
        """
        raise NotImplementedError


    @abstractmethod
    async def stop(self) -> None:
        """
        Shutdown provider.
        """
        raise NotImplementedError


    @abstractmethod
    async def run(self) -> None:
        """
        Main provider execution loop.
        """
        raise NotImplementedError