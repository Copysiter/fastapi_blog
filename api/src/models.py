from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel, Field

from .utils import PyObjectId


class PostModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    slug: str = Field(...)
    categories: List[str] = Field(...)
    body: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}


class UpdatedPostModel(BaseModel):
    title: Optional[str]
    slug: Optional[str]
    categories: Optional[List[str]]
    body: Optional[str]

    class Config:
        json_encoders = {ObjectId: str}
