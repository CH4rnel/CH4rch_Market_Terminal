# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations


import importlib
import pkgutil
import inspect


from ch4rch_market.providers.base import MarketProvider


class ProviderDiscovery:
    """
    Automatic provider discovery.
    """


    def __init__(
        self,
        event_bus,
    ) -> None:

        self.event_bus = event_bus


    def discover(self) -> list[MarketProvider]:

        providers: list[MarketProvider] = []


        package = importlib.import_module(
            "ch4rch_market.providers"
        )


        for module_info in pkgutil.walk_packages(
            package.__path__,
            package.__name__ + ".",
        ):

            if module_info.name.endswith(
                ".provider"
            ):

                module = importlib.import_module(
                    module_info.name
                )


                for _, obj in inspect.getmembers(
                    module,
                    inspect.isclass,
                ):

                    if (
                        issubclass(
                            obj,
                            MarketProvider
                        )
                        and obj is not MarketProvider
                    ):

                        providers.append(
                            obj(
                                self.event_bus
                            )
                        )


        return providers
