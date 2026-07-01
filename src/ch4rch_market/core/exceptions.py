# ♃ ☿ 𓂀 OCCULT CONFIG LAYER 𓂀 ☿ ♃


# Application exceptions.


class CH4rchError(Exception):

#  Base application exception.


    pass


class ConfigurationError(CH4rchError):

#  Configuration loading or validation error.


    pass


class EventBusError(CH4rchError):

# Event bus operation error.


    pass


class ProviderError(CH4rchError):

# Base provider exception.


    pass


class MarketDataError(ProviderError):

# Market data fetch error.


    pass


class ConnectionError(ProviderError):

# External provider connection error.

    pass
