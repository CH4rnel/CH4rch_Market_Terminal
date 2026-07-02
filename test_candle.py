from ch4rch_market.storage.models.candle import Candle


candle = Candle(
    exchange="binance",
    symbol="BTCUSDT",
    timeframe="1m",
    open=120000,
    high=120500,
    low=119900,
    close=120300,
    volume=42.5,
)

print(candle.model_dump())
