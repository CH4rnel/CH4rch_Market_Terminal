# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃


from ch4rch_market.providers.base import (
    Provider,
    ProviderState,
)


class MockProvider(Provider):


    name = "mock"


    async def start(self) -> None:

        self.state = ProviderState.STARTING

        self.state = ProviderState.RUNNING



    async def stop(self) -> None:

        self.state = ProviderState.STOPPING

        self.state = ProviderState.STOPPED
