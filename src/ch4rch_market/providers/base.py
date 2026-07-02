# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃


# Base provider interface.


from abc import ABC, abstractmethod

from ch4rch_market.core.event_bus import EventBus


class BaseProvider(ABC):

# Base class for all market data providers.


    def __init__(
        self,
        event_bus: EventBus,
    ) -> None:
        self.event_bus = event_bus

    @property
    @abstractmethod
    def name(self) -> str:

# Provider name.

        ...

    @abstractmethod
    async def start(self) -> None:

# Start provider.
        ...

    @abstractmethod
    async def stop(self) -> None:

# Stop provider.

        ...
