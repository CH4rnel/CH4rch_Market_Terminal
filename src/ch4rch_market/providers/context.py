# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from ch4rch_market.config.settings import AppSettings
from ch4rch_market.core.event_bus import EventBus

if TYPE_CHECKING:
    from structlog.stdlib import BoundLogger


@dataclass(slots=True)
class ProviderContext:
    """
    Shared runtime context passed to every provider.
    """

    settings: AppSettings
    logger: BoundLogger
    event_bus: EventBus
