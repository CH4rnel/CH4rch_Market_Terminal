# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from ch4rch_market.providers.provider import Provider


class ProviderRegistry:
    """
    Stores market providers.
    """


    def __init__(self) -> None:

        self._providers: dict[
            str,
            Provider,
        ] = {}


    def register(
        self,
        provider: Provider,
    ) -> None:

        if provider.name in self._providers:
            raise ValueError(
                f"Provider {provider.name} exists"
            )

        self._providers[
            provider.name
        ] = provider


    def get(
        self,
        name: str,
    ) -> Provider:

        return self._providers[name]


    def all(
        self,
    ) -> list[Provider]:

        return list(
            self._providers.values()
        )
