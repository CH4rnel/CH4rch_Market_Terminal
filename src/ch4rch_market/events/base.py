# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import UUID
from uuid import uuid4


@dataclass(slots=True)
class Event:
    """
    Base application event.
    """

    id: UUID = uuid4()

    timestamp: datetime = datetime.now(
        timezone.utc
    )
