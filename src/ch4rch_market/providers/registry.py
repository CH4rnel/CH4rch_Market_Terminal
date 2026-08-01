# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from ch4rch_market.providers.base import BaseProvider


class ProviderRegistry:
    """
    Registry and lifecycle manager for market providers.
    """

    def __init__(self) -> None:

        self._providers: dict[str, BaseProvider] = {}

    def register(
        self,
        provider: BaseProvider,
    ) -> None:
        """
        Register provider instance.
        """

        if provider.name in self._providers:
            raise ValueError(
                f"Provider already registered: {provider.name}"
            )

        self._providers[provider.name] = provider

        provider.logger.info(
            "provider_registered",
        )


    def unregister(
        self,
        name: str,
    ) -> None:
        """
        Remove provider from registry.
        """

        self._providers.pop(
            name,
            None,
        )


    def get(
        self,
        name: str,
    ) -> BaseProvider:

        provider = self._providers.get(name)

        if provider is None:
            raise KeyError(
                f"Unknown provider: {name}"
            )

        return provider


    def list(self) -> list[str]:
        """
        Return registered provider names.
        """

        return list(
            self._providers.keys()
        )


    async def start_all(self) -> None:
        """
        Start all registered providers.
        """

        for provider in self._providers.values():

            await provider.start()


    async def stop_all(self) -> None:
        """
        Stop all registered providers.
        """

        for provider in reversed(
            list(self._providers.values())
        ):

            await provider.stop()


    def clear(self) -> None:
        """
        Remove all providers.
        """

        self._providers.clear()
