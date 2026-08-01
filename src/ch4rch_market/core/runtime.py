# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from ch4rch_market.config.settings import settings
from ch4rch_market.core.event_bus import EventBus
from ch4rch_market.core.lifecycle import RuntimeState
from ch4rch_market.core.logger import logger
from ch4rch_market.core.logger import setup_logging
from ch4rch_market.core.modules.manager import ModuleManager
from ch4rch_market.core.modules.system import SystemModule
from ch4rch_market.core.registry import ServiceRegistry
from ch4rch_market.providers.registry import ProviderRegistry


class Runtime:
    """
    Main application runtime.

    Responsible for initializing and controlling
    application subsystems.
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

        self.provider_registry = ProviderRegistry()

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

        self.registry.register(
            "providers",
            self.provider_registry,
        )


        self.module_manager.register(
            SystemModule()
        )


        self.state = RuntimeState.STARTING


        self.logger.info(
            "runtime_started",
            version=self.settings.version,
        )


        await self.module_manager.start_all()


        await self.provider_registry.start_all()


        self.state = RuntimeState.RUNNING


        self.logger.info(
            "runtime_running",
        )


    async def stop(self) -> None:

        self.state = RuntimeState.STOPPING


        self.logger.info(
            "runtime_stopping",
        )


        await self.provider_registry.stop_all()


        await self.module_manager.stop_all()


        self.registry.clear()


        self.state = RuntimeState.STOPPED


        self.logger.info(
            "runtime_stopped",
        )
