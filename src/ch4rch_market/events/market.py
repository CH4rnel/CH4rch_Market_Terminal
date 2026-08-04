# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ch4rch_market.events.base import Event


@dataclass
class MarketEvent(Event):
    """
    Base market event.
    """

    symbol: str



@dataclass
class TickerEvent(MarketEvent):
    """
    Real-time ticker update.
    """

    price: Decimal

    volume: Decimal



@dataclass
class CandleEvent(MarketEvent):
    """
    OHLC candle event.
    """

    timeframe: str

    open: Decimal

    high: Decimal

    low: Decimal

    close: Decimal

    volume: Decimal



@dataclass
class TradeEvent(MarketEvent):
    """
    Executed trade event.
    """

    trade_id: str

    price: Decimal

    amount: Decimal

    side: str