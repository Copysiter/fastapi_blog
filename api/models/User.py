from datetime import datetime
from bson.objectid import ObjectId
from fastapi import Body
from pydantic import BaseModel, EmailStr, Field

from utils import PyObjectId


class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str = Body(...)
    email: EmailStr = Body(...)
    password: str = Body(...)
    created_at: datetime = Field(default=datetime.now())

    class Config:
        json_encoders = {
            ObjectId: str
        }


class UserOutModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str
    email: EmailStr
    created_at: datetime = Field(default=datetime.now())

    class Config:
        json_encoders = {
            ObjectId: str
        }
