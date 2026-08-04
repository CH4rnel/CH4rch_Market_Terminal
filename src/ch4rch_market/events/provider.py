# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from dataclasses import dataclass

from ch4rch_market.events.base import Event


@dataclass(slots=True, kw_only=True)
class ProviderEvent(Event):
    """
    Base provider lifecycle event.
    """

    provider: str


@dataclass(slots=True, kw_only=True)
class ProviderStartedEvent(ProviderEvent):
    """
    Provider started successfully.
    """

    event_type: str = "provider.started"


@dataclass(slots=True, kw_only=True)
class ProviderStoppedEvent(ProviderEvent):
    """
    Provider stopped gracefully.
    """

    event_type: str = "provider.stopped"


@dataclass(slots=True, kw_only=True)
class ProviderErrorEvent(ProviderEvent):
    """
    Provider runtime error.
    """

    message: str

    event_type: str = "provider.error"