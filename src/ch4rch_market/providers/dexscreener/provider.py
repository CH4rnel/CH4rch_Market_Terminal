# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations


from ch4rch_market.providers.base import MarketProvider
from ch4rch_market.events.provider import ProviderStartedEvent, ProviderStoppedEvent



class DexScreenerProvider(MarketProvider):

    name = "dexscreener"


    async def start(self) -> None:

        await self.event_bus.publish(
            ProviderStartedEvent(
                provider=self.name,
            )
        )


    async def stop(self) -> None:

        await self.event_bus.publish(
            ProviderStoppedEvent(
                provider=self.name,
            )
        )
