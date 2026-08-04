# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime



@dataclass(slots=True)
class Event:
    """
    Base event type.
    """

    event_type: str = field(
        default="event",
        init=False,
    )

    created_at: datetime = field(
        default_factory=datetime.utcnow,
        init=False,
    )