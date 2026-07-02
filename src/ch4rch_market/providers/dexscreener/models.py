# ♃ ☿ 𓂀 OCCULT CONFIG LAYER 𓂀 ☿ ♃


# DexScreener models.


from pydantic import BaseModel, ConfigDict, Field


class TokenInfo(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    symbol: str
    name: str
    address: str


class PairInfo(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    chain_id: str = Field(alias="chainId")
    dex_id: str = Field(alias="dexId")

    price_usd: str = Field(alias="priceUsd")

    base_token: TokenInfo = Field(alias="baseToken")
    quote_token: TokenInfo = Field(alias="quoteToken")
