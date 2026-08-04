# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from ch4rch_market.providers.base import MarketProvider


class DexScreenerProvider(MarketProvider):

    name = "dexscreener"


    async def start(self) -> None:

        self.running = True


    async def stop(self) -> None:

        self.running = False


    async def run(self) -> None:
        """
        DexScreener background loop.
        """

        while self.running:

            # TODO:
            # websocket / REST polling
            # market events publishing

            break