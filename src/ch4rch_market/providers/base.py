# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from abc import ABC, abstractmethod

from ch4rch_market.core.event_bus import EventBus


class MarketProvider(ABC):
    """
    Base market data provider interface.
    """

    name: str = "unknown"

    def __init__(
        self,
        event_bus: EventBus,
    ) -> None:

        self.event_bus = event_bus

    @abstractmethod
    async def start(self) -> None:
        """
        Start provider.
        """
        raise NotImplementedError

    @abstractmethod
    async def stop(self) -> None:
        """
        Stop provider.
        """
        raise NotImplementedError
