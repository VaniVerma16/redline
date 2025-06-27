from pydantic import BaseModel
from typing import Literal
from datetime import datetime

class Transaction(BaseModel):
    id: str
    amount: float
    currency: str
    card_id: str
    ip: str
    timestamp: datetime
