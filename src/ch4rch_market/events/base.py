# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from dataclasses import dataclass



@dataclass(slots=True)
class Event:
    """
    Base event class.

    All internal events inherit from this.
    """

    event_type: str
