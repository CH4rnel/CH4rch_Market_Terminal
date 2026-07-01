# ♃ ☿ 𓂀 OCCULT CONFIG LAYER 𓂀 ☿ ♃

# Base application events.


from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import uuid4


@dataclass(slots=True)
class BaseEvent:

# Base event for all application events.


    event_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )


@dataclass(slots=True)
class MarketEvent(BaseEvent):

# Market data event.


    provider: str = ""
    symbol: str = ""
