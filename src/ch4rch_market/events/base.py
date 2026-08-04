# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime


@dataclass(slots=True, kw_only=True)
class Event:
    """
    Base event for the internal event bus.

    Every event in the system must inherit from this class.
    """

    event_type: str

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )