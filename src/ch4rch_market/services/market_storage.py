# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations


from ch4rch_market.core.event_bus import EventBus
from ch4rch_market.core.logger import logger

from ch4rch_market.events.market import (
    TickerEvent,
    CandleEvent,
    TradeEvent,
)


class MarketStorageService:
    """
    Consumes market events and prepares them
    for persistent storage.
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
            "ticker",
            self.handle_ticker,
        )

        self.event_bus.subscribe(
            "candle",
            self.handle_candle,
        )

        self.event_bus.subscribe(
            "trade",
            self.handle_trade,
        )

        logger.info(
            "market_storage_started",
        )


    async def stop(
        self,
    ) -> None:

        logger.info(
            "market_storage_stopped",
        )


    async def handle_ticker(
        self,
        event: TickerEvent,
    ) -> None:

        logger.info(
            "ticker_received",
            symbol=event.symbol,
            price=str(event.price),
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