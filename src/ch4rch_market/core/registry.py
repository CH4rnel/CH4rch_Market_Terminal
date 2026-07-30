# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

from typing import Any


class ServiceRegistry:
    """Simple runtime service registry."""

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}

    def register(
        self,
        name: str,
        service: Any,
    ) -> None:

        if name in self._services:
            raise KeyError(
                f"Service '{name}' already registered."
            )

        self._services[name] = service

    def get(
        self,
        name: str,
    ) -> Any:

        try:
            return self._services[name]

        except KeyError as exc:
            raise KeyError(
                f"Unknown service '{name}'."
            ) from exc

    def unregister(
        self,
        name: str,
    ) -> None:

        self._services.pop(name, None)

    def clear(self) -> None:
        self._services.clear()
