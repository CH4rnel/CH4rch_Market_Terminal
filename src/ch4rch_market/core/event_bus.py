# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃


# Asynchronous event bus implementation.


from collections import defaultdict
from collections.abc import Awaitable, Callable

from ch4rch_market.events.base import Event


EventHandler = Callable[[Event], Awaitable[None]]


class EventBus:

# Simple asynchronous event bus.


    def __init__(self) -> None:
        self._handlers: dict[str, list[EventHandler]] = defaultdict(list)

    def subscribe(
        self,
        event_type: str,
        handler: EventHandler,
    ) -> None:

# Register event handler.


        if handler not in self._handlers[event_type]:
            self._handlers[event_type].append(handler)

    def unsubscribe(
        self,
        event_type: str,
        handler: EventHandler,
    ) -> None:

# Remove event handler.


        if handler in self._handlers[event_type]:
            self._handlers[event_type].remove(handler)

    async def publish(
        self,
        event: Event,
    ) -> None:

# Publish event to all subscribers.


        handlers = self._handlers.get(
            event.event_type,
            [],
        )

        for handler in handlers:
            try:
                await handler(event)

            except Exception as error:
                print(
                    f"Event handler failed: {error}"
                )
