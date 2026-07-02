# ♃ ☿ 𓂀 CANDLE MODEL LAYER 𓂀 ☿ ♃


from datetime import UTC
from datetime import datetime

from pydantic import BaseModel
from pydantic import Field


class Candle(BaseModel):

    # Market candle model.

    exchange: str
    symbol: str
    timeframe: str

    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
    )

    open: float
    high: float
    low: float
    close: float
    volume: float
