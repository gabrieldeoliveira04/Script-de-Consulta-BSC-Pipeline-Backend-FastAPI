from pydantic import BaseModel
from datetime import datetime


class BalanceResponse(BaseModel):

    wallet_address: str

    token_address: str

    balance: float

    collected_at: datetime


    class Config:

        from_attributes = True