# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃


# DexScreener provider.


from ch4rch_market.providers.base import BaseProvider


class DexScreenerProvider(BaseProvider):

# DexScreener market data provider.


    @property
    def name(self) -> str:
        return "dexscreener"

    async def start(self) -> None:
        print(f"{self.name}: started")

    async def stop(self) -> None:
        print(f"{self.name}: stopped")
