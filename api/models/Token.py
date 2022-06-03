from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
