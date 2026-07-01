# ♃ ☿ 𓂀 OCCULT CONFIG LAYER 𓂀 ☿ ♃


# DexScreener provider.


from ch4rch_market.providers.base import BaseProvider
from ch4rch_market.providers.dexscreener.client import (
    DexScreenerClient,
)


class DexScreenerProvider(BaseProvider):

    name = "dexscreener"

    def __init__(self) -> None:

        self.client = DexScreenerClient()

    async def connect(self) -> None:

        pass

    async def close(self) -> None:

        await self.client.close()

    async def healthcheck(self) -> bool:

        return True
