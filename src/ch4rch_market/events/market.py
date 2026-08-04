# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from dataclasses import dataclass

from ch4rch_market.events.base import Event


@dataclass(slots=True, kw_only=True)
class MarketEvent(Event):
    """
    Base class for all market events.
    """

    symbol: str


@dataclass(slots=True, kw_only=True)
class TickerEvent(MarketEvent):
    """
    Real-time ticker update.
    """

    price: float

    volume: float

    event_time: int

    event_type: str = "market.ticker"


@dataclass(slots=True, kw_only=True)
class TradeEvent(MarketEvent):
    """
    Real-time trade event.
    """

    price: float

    quantity: float

    trade_id: int

    buyer_maker: bool

    event_time: int

    event_type: str = "market.trade"


@dataclass(slots=True, kw_only=True)
class CandleEvent(MarketEvent):
    """
    OHLCV candle update.
    """

    interval: str

    open: float

    high: float

    low: float

    close: float

    volume: float

    open_time: int

    close_time: int

    closed: bool

    event_type: str = "market.candle"