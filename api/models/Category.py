from datetime import datetime
from typing import List
from pydantic import BaseModel, Field

from api.utils import PyObjectId


class CategoryModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
