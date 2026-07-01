# ♃ ☿ 𓂀 OCCULT CONFIG LAYER 𓂀 ☿ ♃


# DexScreener HTTP client.


import httpx


class DexScreenerClient:

    BASE_URL = "https://api.dexscreener.com/latest"

    def __init__(self) -> None:

        self._client = httpx.AsyncClient(
            timeout=10,
        )

    async def close(self) -> None:

        await self._client.aclose()

    async def get_pair(
        self,
        chain: str,
        pair_address: str,
    ) -> dict:

        url = (
            f"{self.BASE_URL}"
            f"/dex/pairs/{chain}/{pair_address}"
        )

        response = await self._client.get(url)

        response.raise_for_status()

        return response.json()
