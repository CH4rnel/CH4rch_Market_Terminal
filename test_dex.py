# ♃ ☿ 𓂀 OCCULT CONFIG LAYER 𓂀 ☿ ♃

import asyncio
import json

from ch4rch_market.providers.dexscreener.client import (
    DexScreenerClient,
)


SOL_USDC_PAIR = "9wFFmGphzaYdVQwN3Z6sP1J5X6zA9Qh7R9P7wR7J7F2"


async def main():

    client = DexScreenerClient()

    data = await client.get_pair(
        chain="solana",
        pair_address=SOL_USDC_PAIR,
    )

    print(json.dumps(data, indent=2))

    await client.close()


asyncio.run(main())
