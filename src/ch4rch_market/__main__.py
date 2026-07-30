# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

import asyncio

from ch4rch_market.core.runtime import Runtime


async def run() -> None:

    runtime = Runtime()

    try:
        await runtime.start()

    finally:
        await runtime.stop()


def main() -> None:

    asyncio.run(
        run(),
    )


if __name__ == "__main__":
    main()
