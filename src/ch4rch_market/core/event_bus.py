# ♃ ☿ 𓂀 OCCULT CONFIG LAYER 𓂀 ☿ ♃


# Application event bus.


from collections import defaultdict
from collections.abc import Callable

from ch4rch_market.core.events import BaseEvent


EventHandler = Callable[[BaseEvent], None]


class EventBus:

# In-memory synchronous event bus.


    def __init__(self) -> None:

        self._handlers: dict[
            type[BaseEvent],
            list[EventHandler],
        ] = defaultdict(list)

    def subscribe(
        self,
        event_type: type[BaseEvent],
        handler: EventHandler,
    ) -> None:

# Register event handler.


        self._handlers[event_type].append(handler)

    def publish(
        self,
        event: BaseEvent,
    ) -> None:

# Publish event.


        handlers = self._handlers.get(type(event), [])

        for handler in handlers:
            handler(event)
