# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃


# Market events.


from ch4rch_market.events.base import Event


class PriceUpdateEvent(Event):

# Market price update.


    event_type: str = "market.price"

    exchange: str
    symbol: str
    price: float


class OrderBookUpdateEvent(Event):

# Order book update.


    event_type: str = "market.orderbook"

    exchange: str
    symbol: str
    bids: list
    asks: list
