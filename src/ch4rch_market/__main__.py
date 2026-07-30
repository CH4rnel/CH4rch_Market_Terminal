# ♃ ☿ 𓂀 OCCULT CONFIG LAYER 𓂀 ☿ ♃

import asyncio

from ch4rch_market.core.bootstrap import (
    create_runtime,
)

from ch4rch_market.core.logger import (
    setup_logging,
)

from ch4rch_market.config.settings import (
    get_settings,
)


async def run():

    settings = get_settings()

    setup_logging(
        settings.log_level
    )

    runtime = await create_runtime()

    await runtime.start()

    await runtime.stop()



def main():

    asyncio.run(run())


if __name__ == "__main__":
    main()
