# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from ch4rch_market.core.logger import logger

from ch4rch_market.providers.base import Provider
from ch4rch_market.providers.registry import ProviderRegistry


class ProviderManager:
    """
    Controls provider lifecycle.
    """


    def __init__(
        self,
        registry: ProviderRegistry,
    ) -> None:

        self.registry = registry


    def register(
        self,
        provider: Provider,
    ) -> None:

        self.registry.register(provider)

        logger.info(
            "provider_registered",
            provider=provider.name,
        )


    async def start_all(self) -> None:

        for provider in self.registry.all():

            logger.info(
                "provider_starting",
                provider=provider.name,
            )

            await provider.start()

            logger.info(
                "provider_started",
                provider=provider.name,
            )


    async def stop_all(self) -> None:

        for provider in reversed(
            self.registry.all()
        ):

            logger.info(
                "provider_stopping",
                provider=provider.name,
            )

            await provider.stop()

            logger.info(
                "provider_stopped",
                provider=provider.name,
            )
