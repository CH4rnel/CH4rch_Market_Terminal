import asyncio

from ch4rch_market.core.event_bus import EventBus
from ch4rch_market.providers.binance.provider import BinanceProvider
from ch4rch_market.providers.dexscreener.provider import (
    DexScreenerProvider,
)


async def main() -> None:
    bus = EventBus()

    providers = [
        BinanceProvider(bus),
        DexScreenerProvider(bus),
    ]

    for provider in providers:
        await provider.start()

    for provider in providers:
        await provider.stop()


asyncio.run(main())
