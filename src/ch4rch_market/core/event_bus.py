# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations


from collections import defaultdict
from collections.abc import Awaitable, Callable


from ch4rch_market.events.base import Event



EventHandler = Callable[
    [Event],
    Awaitable[None],
]



class EventBus:
    """
    Async internal message bus.
    """


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

            self._handlers[event_type].append(
                handler
            )



    def unsubscribe(
        self,
        event_type: str,
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
            event.event_type,
            [],
        )


        for handler in handlers:

            await handler(event)
