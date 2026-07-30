from ch4rch_market.config.settings import (
    get_settings,
)

from ch4rch_market.core.event_bus import EventBus
from ch4rch_market.core.logger import get_logger

from ch4rch_market.events.system import (
    SystemStarted,
    SystemStopped,
)


class Runtime:


    def __init__(self):

        self.settings = get_settings()

        self.event_bus = EventBus()

        self.logger = get_logger()


    async def start(self):

        self.logger.info(
            "runtime_starting",
            app=self.settings.app_name,
        )

        await self.event_bus.publish(
            SystemStarted()
        )


    async def stop(self):

        await self.event_bus.publish(
            SystemStopped()
        )

        self.logger.info(
            "runtime_stopped"
        )
