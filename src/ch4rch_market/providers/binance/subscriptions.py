# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations


def ticker_stream(
    symbol: str,
) -> str:
    """
    Binance mini ticker stream.
    """

    return f"{symbol.lower()}@miniTicker"


def trade_stream(
    symbol: str,
) -> str:
    """
    Binance trade stream.
    """

    return f"{symbol.lower()}@trade"


def depth_stream(
    symbol: str,
) -> str:
    """
    Binance order book stream.
    """

    return f"{symbol.lower()}@depth"


def multiplex(
    *streams: str,
) -> str:
    """
    Build multiplex websocket path.
    """

    return "/".join(streams)