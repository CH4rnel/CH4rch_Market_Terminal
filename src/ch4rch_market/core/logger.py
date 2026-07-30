# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

import logging

import structlog


def setup_logging(
    level: str = "INFO",
) -> None:

    logging.basicConfig(
        level=level,
        format="%(message)s",
    )

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(
                fmt="iso"
            ),
            structlog.processors.add_log_level,
            structlog.processors.JSONRenderer(),
        ],
    )


def get_logger():

    return structlog.get_logger()
