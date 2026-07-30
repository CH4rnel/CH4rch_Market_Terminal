# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from dataclasses import dataclass

from ch4rch_market.events.base import Event


@dataclass(slots=True)
class ProviderConnected(Event):

    provider: str


@dataclass(slots=True)
class ProviderDisconnected(Event):

    provider: str
