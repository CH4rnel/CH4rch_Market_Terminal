# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from dataclasses import dataclass

from ch4rch_market.events.base import Event


@dataclass(slots=True, kw_only=True)
class SystemEvent(Event):
    """
    Base runtime lifecycle event.
    """


@dataclass(slots=True, kw_only=True)
class RuntimeStartedEvent(SystemEvent):
    """
    Runtime entered RUNNING state.
    """

    version: str

    event_type: str = "runtime.started"


@dataclass(slots=True, kw_only=True)
class RuntimeStoppedEvent(SystemEvent):
    """
    Runtime shutdown completed.
    """

    event_type: str = "runtime.stopped"