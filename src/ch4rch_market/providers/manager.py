# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

import asyncio

from ch4rch_market.core.event_bus import EventBus
from ch4rch_market.core.logger import logger
from ch4rch_market.providers.base import MarketProvider


class ProviderManager:
    """
    Async lifecycle manager for market providers.
    """

    def __init__(
        self,
        event_bus: EventBus,
    ) -> None:

        self.event_bus = event_bus

        self._providers: list[MarketProvider] = []

        self._tasks: list[asyncio.Task] = []


    def register(
        self,
        provider: MarketProvider,
    ) -> None:

        self._providers.append(provider)

        logger.info(
            "provider_registered",
            provider=provider.name,
        )


    async def start_all(self) -> None:
        """
        Start all providers.
        """

        for provider in self._providers:

            logger.info(
                "provider_start",
                provider=provider.name,
            )

            await provider.start()

            task = asyncio.create_task(
                self._run_provider(provider)
            )

            self._tasks.append(task)


    async def _run_provider(
        self,
        provider: MarketProvider,
    ) -> None:

        try:

            await provider.run()

        except Exception as error:

            logger.error(
                "provider_failed",
                provider=provider.name,
                error=str(error),
            )


    async def stop_all(self) -> None:
        """
        Stop all providers.
        """

        for provider in reversed(self._providers):

            logger.info(
                "provider_stop",
                provider=provider.name,
            )

            await provider.stop()


        for task in self._tasks:

            if not task.done():

                task.cancel()


        self._tasks.clear()