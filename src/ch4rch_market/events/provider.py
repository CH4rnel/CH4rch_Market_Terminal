# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃


# Provider events.


from ch4rch_market.events.base import Event


class ProviderConnectedEvent(Event):

# Provider connected.


    event_type: str = "provider.connected"

    provider: str


class ProviderDisconnectedEvent(Event):

# Provider disconnected.


    event_type: str = "provider.disconnected"

    provider: str
