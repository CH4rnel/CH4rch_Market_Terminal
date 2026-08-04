# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations


from ch4rch_market.config.settings import settings

from ch4rch_market.core.event_bus import EventBus
from ch4rch_market.core.lifecycle import RuntimeState
from ch4rch_market.core.logger import (
    logger,
    setup_logging,
)

from ch4rch_market.core.registry import ServiceRegistry

from ch4rch_market.core.modules.manager import (
    ModuleManager,
)

from ch4rch_market.core.modules.system import (
    SystemModule,
)

from ch4rch_market.providers.discovery import (
    ProviderDiscovery,
)

from ch4rch_market.providers.manager import (
    ProviderManager,
)

from ch4rch_market.services.market_storage import (
    MarketStorageService,
)

from ch4rch_market.storage import (
    Database,
    SQLiteManager,
)

class Runtime:
    """
    Main application runtime.
    """


    def __init__(
        self,
    ) -> None:


        self.settings = settings


        setup_logging(
            self.settings.log_level,
        )


        self.logger = logger


        self.event_bus = EventBus()


        self.registry = ServiceRegistry()


        self.state = RuntimeState.CREATED


        self.module_manager = ModuleManager()


        self.module_manager.register(
            SystemModule(),
        )


        self.provider_manager = ProviderManager(
            self.event_bus,
        )


        self.provider_discovery = ProviderDiscovery(
            self.event_bus,
        )


        self.market_storage = MarketStorageService(
            self.event_bus,
        )

        self.database = Database(
        "data/ch4rch_market.db",
        )


        self.sqlite = SQLiteManager(
            self.database,
        )

    async def start(
        self,
    ) -> None:


        self.state = RuntimeState.STARTING


        self.registry.register(
            "settings",
            self.settings,
        )


        self.registry.register(
            "event_bus",
            self.event_bus,
        )


        self.registry.register(
            "logger",
            self.logger,
        )


        self.provider_discovery.discover()


        await self.module_manager.start_all()


        await self.market_storage.start()


        await self.provider_manager.start_all()


        self.state = RuntimeState.RUNNING


        self.logger.info(
            "runtime_running",
        )



    async def stop(
        self,
    ) -> None:


        self.state = RuntimeState.STOPPING


        self.logger.info(
            "runtime_stopping",
        )


        await self.provider_manager.stop_all()


        await self.market_storage.stop()


        await self.module_manager.stop_all()


        self.registry.clear()


        self.state = RuntimeState.STOPPED


        self.logger.info(
            "runtime_stopped",
        )