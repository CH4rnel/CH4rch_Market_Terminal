# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

import asyncio

from ch4rch_market.core.logger import logger
from ch4rch_market.providers.base import MarketProvider
from ch4rch_market.providers.registry import ProviderRegistry


class ProviderManager:
    """Runs and supervises provider lifecycle."""

    def __init__(
        self,
        registry: ProviderRegistry,
    ) -> None:

        self.registry = registry

        self._tasks: dict[str, asyncio.Task] = {}

    async def start(self) -> None:

        for provider in self.registry.providers.values():

            logger.info(
                "provider_start",
                provider=provider.name,
            )

            await provider.start()

            self._tasks[provider.name] = asyncio.create_task(
                provider.run(),
                name=provider.name,
            )

    async def stop(self) -> None:

        for task in self._tasks.values():

            task.cancel()

        for task in self._tasks.values():

            try:
                await task

            except asyncio.CancelledError:
                pass

        for provider in reversed(
            list(self.registry.providers.values())
        ):

            logger.info(
                "provider_stop",
                provider=provider.name,
            )

            await provider.stop()

        self._tasks.clear()
