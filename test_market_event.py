# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from ch4rch_market.events.market import PriceUpdateEvent


event = PriceUpdateEvent(
    exchange="binance",
    symbol="BTCUSDT",
    price=120000,
)

print(event.model_dump())
