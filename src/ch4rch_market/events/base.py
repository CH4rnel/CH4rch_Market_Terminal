# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar



@dataclass
class Event:
    """
    Base application event.
    """

    event_type: ClassVar[str] = "event"
