# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

import logging

import structlog


def setup_logging(
    level: str = "INFO",
) -> None:
    """Configure application logging."""

    logging.basicConfig(
        level=level,
        format="%(message)s",
    )

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.add_log_level,
            structlog.processors.JSONRenderer(),
        ],
    )


logger = structlog.get_logger()
