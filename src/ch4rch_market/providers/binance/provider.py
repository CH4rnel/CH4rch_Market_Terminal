# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

"""
Market provider implementation.

Generates normalized ticker events
and publishes them through EventBus.
"""

from __future__ import annotations

import asyncio
from datetime import datetime, timezone
import random

from ch4rch_market.core.event_bus import EventBus
from ch4rch_market.core.logger import logger
from ch4rch_market.events.market import TickerEvent
from ch4rch_market.providers.base import Provider


class MarketProvider(Provider):
    """
    Basic market data provider.

    Current implementation:
    - mock ticker stream
    - EventBus publishing

    Future:
    - Binance websocket
    - DexScreener API
    - Pump.fun feeds
    """


    def __init__(
        self,
        event_bus: EventBus,
    ) -> None:

        super().__init__()

        self.event_bus = event_bus

        self._task: asyncio.Task | None = None

        self._price = 60000.0



    @property
    def name(self) -> str:

        return "market"



    async def initialize(self) -> None:

        logger.info(
            "market_provider_initialized"
        )



    async def start(self) -> None:

        await super().start()

        self._task = asyncio.create_task(
            self._market_loop()
        )



    async def stop(self) -> None:

        if self._task:

            self._task.cancel()

            try:

                await self._task

            except asyncio.CancelledError:

                pass


        await super().stop()



    async def _market_loop(self) -> None:
        """
        Internal market data loop.

        Produces normalized ticker events.
        """


        while True:

            try:

                # mock price movement

                self._price += random.uniform(
                    -20,
                    20,
                )


                event = TickerEvent(
                    event_type="ticker",
                    symbol="BTCUSDT",
                    timestamp=datetime.now(
                        timezone.utc
                    ),
                    price=round(
                        self._price,
                        2,
                    ),
                    volume=1000,
                )


                await self.event_bus.publish(
                    event
                )


                await asyncio.sleep(
                    1
                )


            except asyncio.CancelledError:

                logger.info(
                    "market_loop_cancelled"
                )

                break


            except Exception as error:

                logger.error(
                    "market_loop_error",
                    error=str(error),
                )

                await asyncio.sleep(
                    5
                )
