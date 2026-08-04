# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Event:
    """
    Base application event.
    """

    event_type: str