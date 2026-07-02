# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃


# Binance provider.


from ch4rch_market.providers.base import BaseProvider


class BinanceProvider(BaseProvider):

# Binance market data provider.


    @property
    def name(self) -> str:
        return "binance"

    async def start(self) -> None:
        print(f"{self.name}: started")

    async def stop(self) -> None:
        print(f"{self.name}: stopped")
