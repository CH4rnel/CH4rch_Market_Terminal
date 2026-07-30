# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from dataclasses import dataclass

from ch4rch_market.events.base import Event


@dataclass(slots=True)
class SystemStarted(Event):
    pass


@dataclass(slots=True)
class SystemStopped(Event):
    pass
