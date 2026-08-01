# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from dataclasses import dataclass

from ch4rch_market.events.base import Event



@dataclass
class ProviderStartedEvent(Event):

    provider: str

    event_type = "provider_started"



@dataclass
class ProviderStoppedEvent(Event):

    provider: str

    event_type = "provider_stopped"
