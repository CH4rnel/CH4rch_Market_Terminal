# ♃ ☿ 𓂀 OCCULT CONFIG LAYER 𓂀 ☿ ♃


# DexScreener models.


from pydantic import BaseModel


class TokenInfo(BaseModel):

    symbol: str
    name: str
    address: str


class PairInfo(BaseModel):

    chain_id: str
    dex_id: str

    price_usd: float

    base_token: TokenInfo
    quote_token: TokenInfo
