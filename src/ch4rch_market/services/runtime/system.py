# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from ch4rch_market.core.logger import logger
from ch4rch_market.core.modules.base import Module


class SystemModule(Module):
    """Basic runtime system module."""

    @property
    def name(self) -> str:
        return "system"

    async def start(self) -> None:

        logger.info(
            "system_module_started",
        )

    async def stop(self) -> None:

        logger.info(
            "system_module_stopped",
        )
