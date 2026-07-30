# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from ch4rch_market.core.logger import logger
from ch4rch_market.core.modules.base import Module


class ModuleManager:
    """Runtime module manager."""

    def __init__(self) -> None:
        self._modules: list[Module] = []

    def register(
        self,
        module: Module,
    ) -> None:

        self._modules.append(module)

        logger.info(
            "module_registered",
            module=module.name,
        )

    async def start_all(self) -> None:

        for module in self._modules:

            logger.info(
                "module_start",
                module=module.name,
            )

            await module.start()

    async def stop_all(self) -> None:

        for module in reversed(self._modules):

            logger.info(
                "module_stop",
                module=module.name,
            )

            await module.stop()
