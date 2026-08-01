# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ch4rch_market.events.base import Event


@dataclass(slots=True)
class MarketEvent(Event):
    """
    Base market event.
    """

    symbol: str

    def __post_init__(self) -> None:
        self.event_type = "market"


@dataclass(slots=True)
class TickerEvent(MarketEvent):
    """
    Real-time ticker update.
    """

    price: Decimal
    volume: Decimal

    def __post_init__(self) -> None:
        self.event_type = "ticker"


@dataclass(slots=True)
class CandleEvent(MarketEvent):
    """
    OHLC candle update.
    """

    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: Decimal
    timeframe: str

    def __post_init__(self) -> None:
        self.event_type = "candle"
