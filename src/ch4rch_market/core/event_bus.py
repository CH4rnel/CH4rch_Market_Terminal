# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

import asyncio

from collections import defaultdict
from collections.abc import Awaitable, Callable

import structlog

from ch4rch_market.events.base import Event


logger = structlog.get_logger()


EventHandler = Callable[
    [Event],
    Awaitable[None]
]


class EventBus:

    def __init__(self) -> None:
        self._handlers: dict[
            str,
            list[EventHandler]
        ] = defaultdict(list)


    def subscribe(
        self,
        event_type: str,
        handler: EventHandler,
    ) -> None:

        if handler not in self._handlers[event_type]:
            self._handlers[event_type].append(handler)


    def unsubscribe(
        self,
        event_type: str,
        handler: EventHandler,
    ) -> None:

        handlers = self._handlers.get(event_type)

        if handlers and handler in handlers:
            handlers.remove(handler)


    async def publish(
        self,
        event: Event,
    ) -> None:

        handlers = self._handlers.get(
            event.event_type,
            [],
        )

        if not handlers:
            return


        tasks = [
            handler(event)
            for handler in handlers
        ]


        results = await asyncio.gather(
            *tasks,
            return_exceptions=True,
        )


        for result in results:

            if isinstance(
                result,
                Exception,
            ):
                logger.error(
                    "event_handler_failed",
                    error=str(result),
                )
