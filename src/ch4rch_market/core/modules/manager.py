# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from ch4rch_market.core.logger import logger
from ch4rch_market.core.modules.base import Module


class ModuleManager:
    """
    Runtime module manager.

    Responsible for:
    - module registration
    - module lookup
    - lifecycle control
    """

    def __init__(self) -> None:

        self._modules: dict[str, Module] = {}


    def register(
        self,
        module: Module,
    ) -> None:
        """
        Register module.

        Module names must be unique.
        """

        if module.name in self._modules:
            raise ValueError(
                f"Module '{module.name}' already registered"
            )

        self._modules[module.name] = module

        logger.info(
            "module_registered",
            module=module.name,
        )


    def get(
        self,
        name: str,
    ) -> Module:
        """
        Get module by name.
        """

        return self._modules[name]


    async def start_all(self) -> None:
        """
        Start all registered modules.
        """

        for module in self._modules.values():

            logger.info(
                "module_start",
                module=module.name,
            )

            await module.start()


    async def stop_all(self) -> None:
        """
        Stop all registered modules.

        Modules are stopped in reverse order.
        """

        for module in reversed(
            list(self._modules.values())
        ):

            logger.info(
                "module_stop",
                module=module.name,
            )

            await module.stop()
