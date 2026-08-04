# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations

import asyncio

from ch4rch_market.core.logger import logger
from ch4rch_market.events.base import Event
from ch4rch_market.providers.base import MarketProvider


class BaseStreamingProvider(MarketProvider):
    """
    Base class for streaming market providers.

    Handles:
    - lifecycle
    - reconnect loop
    - exception handling
    - event publishing
    """

    reconnect_delay: float = 5.0


    def __init__(
        self,
        event_bus,
    ) -> None:

        super().__init__(
            event_bus,
        )

        self._running = False


    async def start(self) -> None:
        """
        Start provider.
        """

        self._running = True

        logger.info(
            "streaming_provider_started",
            provider=self.name,
        )


    async def stop(self) -> None:
        """
        Stop provider.
        """

        self._running = False

        logger.info(
            "streaming_provider_stopped",
            provider=self.name,
        )


    async def run(self) -> None:
        """
        Main streaming loop.
        """

        while self._running:

            try:

                await self.connect()

                while self._running:

                    payload = await self.receive()

                    event = self.parse(
                        payload,
                    )

                    if event is not None:

                        await self.event_bus.publish(
                            event,
                        )


            except asyncio.CancelledError:

                break


            except Exception as error:

                logger.error(
                    "provider_stream_error",
                    provider=self.name,
                    error=str(error),
                )

                await asyncio.sleep(
                    self.reconnect_delay,
                )


            finally:

                await self.disconnect()


    async def connect(self) -> None:
        """
        Open connection.

        Must be implemented by provider.
        """

        raise NotImplementedError


    async def disconnect(self) -> None:
        """
        Close connection.

        Must be implemented by provider.
        """

        raise NotImplementedError


    async def receive(self) -> dict:
        """
        Receive raw provider payload.
        """

        raise NotImplementedError


    def parse(
        self,
        payload: dict,
    ) -> Event | None:
        """
        Convert provider payload into domain event.
        """

        raise NotImplementedError