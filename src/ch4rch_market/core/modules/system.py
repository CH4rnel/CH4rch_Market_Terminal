# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from ch4rch_market.core.modules.base import Module
from ch4rch_market.core.logger import logger


class SystemModule(Module):
    """
    Core system lifecycle module.
    """

    name = "system"

    async def start(self) -> None:

        logger.info(
            "system_module_started",
        )


    async def stop(self) -> None:

        logger.info(
            "system_module_stopped",
        )
