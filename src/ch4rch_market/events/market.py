# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from dataclasses import dataclass

from ch4rch_market.events.base import Event



@dataclass(slots=True)
class MarketEvent(Event):
    """
    Base market event.
    """

    symbol: str



@dataclass(slots=True)
class TickerEvent(MarketEvent):
    """
    Live ticker update.
    """

    price: float

    volume: float

    def __post_init__(self) -> None:

        self.event_type = "ticker"



@dataclass(slots=True)
class CandleEvent(MarketEvent):
    """
    OHLC candle event.
    """

    timeframe: str

    open: float
    high: float
    low: float
    close: float

    volume: float


    def __post_init__(self) -> None:

        self.event_type = "candle"



@dataclass(slots=True)
class TradeEvent(MarketEvent):
    """
    Executed trade event.
    """

    trade_id: str

    price: float

    quantity: float

    side: str


    def __post_init__(self) -> None:

        self.event_type = "trade"