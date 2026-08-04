# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

import asyncio

from ch4rch_market.core.event_bus import EventBus
from ch4rch_market.core.logger import logger

from ch4rch_market.core.modules.manager import ModuleManager
from ch4rch_market.core.modules.system import SystemModule

from ch4rch_market.providers.discovery import ProviderDiscovery
from ch4rch_market.providers.manager import ProviderManager

from ch4rch_market.storage import (
    Database,
    SQLiteManager,
)

from ch4rch_market.services.runtime import (
    StorageService,
)


class Runtime:
    """
    Main application runtime.
    """


    def __init__(self) -> None:

        self.state = "created"


        self.event_bus = EventBus()


        self.module_manager = ModuleManager()

        self.module_manager.register(
            SystemModule()
        )


        self.database = Database(
            "data/ch4rch_market.db",
        )


        self.sqlite = SQLiteManager(
            self.database,
        )


        self.storage_service = StorageService(
            self.event_bus,
        )


        self.provider_discovery = ProviderDiscovery(
            self.event_bus,
        )

        self.provider_manager = ProviderManager(
            self.event_bus,
        )


    async def start(
        self,
    ) -> None:

        self.state = "starting"


        #
        # Database
        #

        await self.sqlite.start()


        #
        # Storage event consumers
        #

        await self.storage_service.start()



        #
        # Modules
        #

        await self.module_manager.start_all()



        #
        # Providers
        #

        providers = self.provider_discovery.discover()


        for provider in providers:

            self.provider_manager.register(
                provider
            )


        await self.provider_manager.start_all()



        self.state = "running"


        logger.info(
            "runtime_started",
        )


        #
        # Keep runtime alive
        #

        while self.state == "running":

            await asyncio.sleep(
                1
            )



    async def stop(
        self,
    ) -> None:

        self.state = "stopping"



        #
        # Providers
        #

        await self.provider_manager.stop_all()



        #
        # Modules
        #

        await self.module_manager.stop_all()



        #
        # Storage
        #

        await self.storage_service.stop()



        #
        # Database
        #

        await self.sqlite.stop()



        self.state = "stopped"


        logger.info(
            "runtime_stopped",
        )