# ♃ ☿ 𓂀 OCCULT CONFIG LAYER 𓂀 ☿ ♃

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class MiniTicker:

    symbol: str

    close: float

    volume: float

    event_time: int