# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃


# Logging configuration for CH4rch Market Terminal.

import logging
import sys

import structlog


def setup_logging() -> None:


# Configure application logging.

    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=logging.INFO,
    )

    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.dev.ConsoleRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(
            logging.INFO,
        ),
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )


def get_logger(name: str):


# Return configured logger instance.

    return structlog.get_logger(name)
