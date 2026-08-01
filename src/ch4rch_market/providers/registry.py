# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from ch4rch_market.providers.base import Provider


class ProviderRegistry:
    """
    Provider dependency registry.
    """

    def __init__(self) -> None:

        self._providers: dict[str, Provider] = {}


    def register(
        self,
        provider: Provider,
    ) -> None:

        self._providers[provider.name] = provider


    def get(
        self,
        name: str,
    ) -> Provider | None:

        return self._providers.get(name)


    def all(self) -> list[Provider]:

        return list(self._providers.values())


    def clear(self) -> None:

        self._providers.clear()
