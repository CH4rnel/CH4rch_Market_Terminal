import asyncio

from ch4rch_market.core.event_bus import (
    BaseEvent,
    EventBus,
)


class TestEvent(BaseEvent):
    message: str


async def handler(event: TestEvent) -> None:
    print(event.message)


async def main() -> None:
    bus = EventBus()

    bus.subscribe(
        "test",
        handler,
    )

    await bus.publish(
        TestEvent(
            event_type="test",
            message="Hello EventBus",
        )
    )


asyncio.run(main())
