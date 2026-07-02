# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃


# Base event models.


from datetime import UTC
from datetime import datetime

from pydantic import BaseModel
from pydantic import Field


class Event(BaseModel):

# Base application event.


    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
    )

    event_type: str
