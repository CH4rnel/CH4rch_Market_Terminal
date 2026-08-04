# ♃ ☿ 𓂀 𓂀 OCCULT CONFIG LAYER 𓂀 ☿ ♃

from __future__ import annotations

import asyncio
import json

import websockets


BINANCE_WS = "wss://stream.binance.com:9443/ws"


class BinanceClient:
    """
    Low-level Binance websocket client.
    """

    def __init__(
        self,
        stream: str,
    ) -> None:

        self.url = f"{BINANCE_WS}/{stream}"

        self.websocket = None

    async def connect(self) -> None:

        self.websocket = await websockets.connect(
            self.url,
            ping_interval=20,
        )

    async def close(self) -> None:

        if self.websocket is not None:

            await self.websocket.close()

    async def receive(self) -> dict:

        message = await self.websocket.recv()

        return json.loads(message)

    async def listen(self):

        while True:

            yield await self.receive()

            await asyncio.sleep(0)