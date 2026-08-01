# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations


from ch4rch_market.config.settings import settings

from ch4rch_market.core.event_bus import EventBus
from ch4rch_market.core.lifecycle import RuntimeState
from ch4rch_market.core.logger import logger
from ch4rch_market.core.logger import setup_logging
from ch4rch_market.core.registry import ServiceRegistry

from ch4rch_market.core.modules.manager import ModuleManager
from ch4rch_market.core.modules.system import SystemModule

from ch4rch_market.providers.discovery import ProviderDiscovery


class Runtime:
    """
    Main application runtime.
    """


    def __init__(self) -> None:

        self.settings = settings

        setup_logging(
            self.settings.log_level,
        )

        self.logger = logger


        self.event_bus = EventBus()


        self.registry = ServiceRegistry()


        self.module_manager = ModuleManager()


        self.provider_discovery = ProviderDiscovery(
            self.event_bus,
        )


        self.providers = []


        self.state = RuntimeState.CREATED



    async def start(self) -> None:

        self.state = RuntimeState.INITIALIZING


        self.registry.register(
            "settings",
            self.settings,
        )


        self.registry.register(
            "logger",
            self.logger,
        )


        self.registry.register(
            "event_bus",
            self.event_bus,
        )


        #
        # Core modules
        #

        self.module_manager.register(
            SystemModule()
        )


        #
        # Providers discovery
        #

        self.providers = (
            self.provider_discovery.discover()
        )


        for provider in self.providers:

            self.logger.info(
                "provider_registered",
                provider=provider.name,
            )


        self.state = RuntimeState.STARTING


        await self.module_manager.start_all()


        for provider in self.providers:

            await provider.start()



        self.logger.info(
            "runtime_started",
            version=self.settings.version,
        )


        self.state = RuntimeState.RUNNING


        self.logger.info(
            "runtime_running",
        )



    async def stop(self) -> None:

        self.state = RuntimeState.STOPPING


        self.logger.info(
            "runtime_stopping",
        )


        for provider in reversed(
            self.providers
        ):

            await provider.stop()



        await self.module_manager.stop_all()



        self.registry.clear()


        self.state = RuntimeState.STOPPED


        self.logger.info(
            "runtime_stopped",
        )
