# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

import asyncio

from ch4rch_market.providers.base import MarketProvider
from ch4rch_market.events.market import TickerEvent

class MockProvider(MarketProvider):
    """
    Mock market data provider.
    Generates fake ticker events.
    """


    name = "mock"



    def __init__(
        self,
        event_bus,
    ) -> None:

        super().__init__(
            event_bus,
        )

        self.running = False
        self.task: asyncio.Task | None = None



    async def start(
        self,
    ) -> None:

        self.running = True


        self.task = asyncio.create_task(
            self.run()
        )



    async def run(
        self,
    ) -> None:

        while self.running:

            event = TickerEvent(
        symbol="BTCUSDT",
        price=50000.0,
        volume=1.0,
        )


            await self.event_bus.publish(
                event,
            )


            await asyncio.sleep(
                5,
            )



    async def stop(
        self,
    ) -> None:

        self.running = False


        if self.task:

            await self.task

            self.task = None