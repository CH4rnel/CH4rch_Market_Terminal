# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

import asyncio


from ch4rch_market.providers.base import BaseProvider
from ch4rch_market.providers.context import ProviderContext


class MockProvider(BaseProvider):
    """
    Internal development provider.

    Generates fake market ticks.
    Used for validating provider lifecycle,
    runtime integration and event flow.
    """


    def __init__(
        self,
        context: ProviderContext,
    ) -> None:

        super().__init__(
            name="mock",
            context=context,
        )

        self._task: asyncio.Task | None = None

        self._running = False


    async def connect(self) -> None:

        self.logger.info(
            "mock_provider_connected",
        )


    async def disconnect(self) -> None:

        self.logger.info(
            "mock_provider_disconnected",
        )


    async def start(self) -> None:

        await super().start()

        self._running = True


        self._task = asyncio.create_task(
            self._market_loop()
        )


    async def stop(self) -> None:

        self._running = False


        if self._task:

            self._task.cancel()

            try:

                await self._task

            except asyncio.CancelledError:

                pass


        await super().stop()



    async def _market_loop(self) -> None:
        """
        Fake market stream.
        Later replaced by websocket providers.
        """


        price = 100.0


        while self._running:


            price += 0.25


            self.logger.info(
                "mock_market_tick",
                symbol="BTCUSDT",
                price=price,
            )


            await asyncio.sleep(5)
