# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from ch4rch_market.providers.context import ProviderContext
from ch4rch_market.providers.lifecycle import ProviderState


class BaseProvider(ABC):
    """
    Base class for every market data provider.
    """

    def __init__(
        self,
        name: str,
        context: ProviderContext,
    ) -> None:

        self._name = name
        self._context = context
        self._state = ProviderState.CREATED

    @property
    def name(self) -> str:
        return self._name

    @property
    def context(self) -> ProviderContext:
        return self._context

    @property
    def state(self) -> ProviderState:
        return self._state

    @property
    def logger(self):
        return self._context.logger.bind(
            provider=self._name,
        )

    @property
    def event_bus(self):
        return self._context.event_bus

    @property
    def settings(self):
        return self._context.settings

    async def start(self) -> None:

        self._state = ProviderState.INITIALIZING

        self.logger.info(
            "provider_initializing",
        )

        await self.connect()

        self._state = ProviderState.RUNNING

        self.logger.info(
            "provider_running",
        )

    async def stop(self) -> None:

        self._state = ProviderState.STOPPING

        self.logger.info(
            "provider_stopping",
        )

        await self.disconnect()

        self._state = ProviderState.STOPPED

        self.logger.info(
            "provider_stopped",
        )

    @abstractmethod
    async def connect(self) -> None:
        """
        Establish provider connection.
        """

    @abstractmethod
    async def disconnect(self) -> None:
        """
        Close provider connection.
        """
