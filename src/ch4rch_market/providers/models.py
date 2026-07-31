# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class MarketPair:
    """
    Normalized trading pair.
    """

    symbol: str
    base: str
    quote: str


@dataclass(slots=True)
class PriceTick:
    """
    Normalized market price update.
    """

    symbol: str
    price: float
    timestamp: datetime
