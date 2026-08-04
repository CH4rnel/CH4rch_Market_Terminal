# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from ch4rch_market.events.market import TickerEvent
from ch4rch_market.providers.binance.client import BinanceClient
from ch4rch_market.providers.binance.parser import parse_message
from ch4rch_market.providers.binance.subscriptions import ticker_stream
from ch4rch_market.providers.streaming import BaseStreamingProvider


class BinanceProvider(
    BaseStreamingProvider,
):
    """
    Binance websocket market provider.
    """

    name = "binance"


    def __init__(
        self,
        event_bus,
        symbol: str = "btcusdt",
    ) -> None:

        super().__init__(
            event_bus,
        )

        self.symbol = symbol

        self.client = BinanceClient(
            ticker_stream(
                symbol,
            )
        )


    async def connect(self) -> None:

        await self.client.connect()


    async def disconnect(self) -> None:

        await self.client.close()


    async def receive(self) -> dict:

        return await self.client.receive()


    def parse(
        self,
        payload: dict,
    ) -> TickerEvent | None:

        ticker = parse_message(
            payload,
        )

        return TickerEvent(
            symbol=ticker.symbol,
            price=ticker.close,
            volume=ticker.volume,
            event_time=ticker.event_time,
        )