# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from ch4rch_market.core.event_bus import EventBus
from ch4rch_market.core.logger import logger

from ch4rch_market.events.market import (
    CandleEvent,
    TradeEvent,
)


class StorageService:
    """
    Stores market events into database.
    """


    def __init__(
        self,
        event_bus: EventBus,
    ) -> None:

        self.event_bus = event_bus


    async def start(
        self,
    ) -> None:

        self.event_bus.subscribe(
            CandleEvent,
            self.handle_candle,
        )


        self.event_bus.subscribe(
            TradeEvent,
            self.handle_trade,
        )


        logger.info(
            "storage_service_started",
        )


    async def stop(
        self,
    ) -> None:

        logger.info(
            "storage_service_stopped",
        )


    async def handle_candle(
        self,
        event: CandleEvent,
    ) -> None:

        logger.info(
            "candle_received",
            symbol=event.symbol,
        )


    async def handle_trade(
        self,
        event: TradeEvent,
    ) -> None:

        logger.info(
            "trade_received",
            symbol=event.symbol,
        )