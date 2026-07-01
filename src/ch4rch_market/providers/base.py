# ♃ ☿ 𓂀 OCCULT CONFIG LAYER 𓂀 ☿ ♃


# Base provider interfaces.


from abc import ABC, abstractmethod


class BaseProvider(ABC):

# Base class for all market providers.


    name: str

    @abstractmethod
    async def connect(self) -> None:

# Initialize provider connection.

        ...

    @abstractmethod
    async def close(self) -> None:

# Close provider connection.

        ...

    @abstractmethod
    async def healthcheck(self) -> bool:

# Check provider availability.

        ...
