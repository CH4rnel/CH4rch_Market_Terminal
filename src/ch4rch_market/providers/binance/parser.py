# ♃ ☿ 𓂀 OCCULT CONFIG LAYER 𓂀 ☿ ♃

from __future__ import annotations

from ch4rch_market.providers.binance.models import MiniTicker


def parse_message(
    payload: dict,
) -> MiniTicker:
    """
    Parse Binance miniTicker payload.
    """

    return MiniTicker(
        symbol=payload["s"],
        close=float(payload["c"]),
        volume=float(payload["v"]),
        event_time=payload["E"],
    )