# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from collections import defaultdict
from collections.abc import Awaitable
from collections.abc import Callable
from typing import Type

from ch4rch_market.events.base import Event
from ch4rch_market.core.logger import logger


EventHandler = Callable[
    [Event],
    Awaitable[None],
]


class EventBus:
    """
    Typed asynchronous event bus.
    """

    def __init__(self) -> None:

        self._handlers: dict[
            Type[Event],
            list[EventHandler],
        ] = defaultdict(list)


    def subscribe(
        self,
        event_type: Type[Event],
        handler: EventHandler,
    ) -> None:

        if handler not in self._handlers[event_type]:
            self._handlers[event_type].append(
                handler
            )


    def unsubscribe(
        self,
        event_type: Type[Event],
        handler: EventHandler,
    ) -> None:

        if handler in self._handlers[event_type]:
            self._handlers[event_type].remove(
                handler
            )


    async def publish(
        self,
        event: Event,
    ) -> None:

        handlers = self._handlers.get(
            type(event),
            [],
        )

        for handler in handlers:

            try:
                await handler(event)

            except Exception as error:

                logger.error(
                    "event_handler_failed",
                    error=str(error),
                    event=type(event).__name__,
                )
