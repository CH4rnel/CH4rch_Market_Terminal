# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from ch4rch_market.config.settings import settings
from ch4rch_market.core.event_bus import EventBus
from ch4rch_market.core.lifecycle import RuntimeState
from ch4rch_market.core.logger import logger
from ch4rch_market.core.logger import setup_logging
from ch4rch_market.core.modules.manager import ModuleManager
from ch4rch_market.core.registry import ServiceRegistry
from ch4rch_market.providers.discovery import ProviderDiscovery
from ch4rch_market.providers.manager import ProviderManager


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


        self.provider_manager = ProviderManager(
            self.event_bus,
        )


        self.state = RuntimeState.CREATED



    async def start(self) -> None:
        """
        Start runtime.
        """

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


        providers = self.provider_discovery.discover()


        for provider in providers:

            self.provider_manager.register(
                provider,
            )


        self.state = RuntimeState.STARTING


        self.logger.info(
            "runtime_started",
            version=self.settings.version,
        )


        await self.module_manager.start_all()


        await self.provider_manager.start_all()


        self.state = RuntimeState.RUNNING


        self.logger.info(
            "runtime_running",
        )



    async def stop(self) -> None:
        """
        Stop runtime.
        """

        self.state = RuntimeState.STOPPING


        self.logger.info(
            "runtime_stopping",
        )


        await self.provider_manager.stop_all()


        await self.module_manager.stop_all()


        self.registry.clear()


        self.state = RuntimeState.STOPPED


        self.logger.info(
            "runtime_stopped",
        )