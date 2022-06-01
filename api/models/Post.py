from datetime import datetime
from typing import List
from pydantic import BaseModel, Field

from utils import PyObjectId


class PostModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    categories: List[str] = Field(...)
    body: str = Field(...)
    created_at: datetime = Field(default_factory=datetime.now)
