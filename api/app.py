from typing import List, Optional
from bson import ObjectId
from fastapi import Body, FastAPI, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import motor.motor_asyncio
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

app = FastAPI()

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
database = client.blog


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="str")


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


@app.get("/")
async def get_root():
    return {"message": "Hello, world!"}


@app.post("/posts/", status_code=status.HTTP_201_CREATED)
async def publish_post(post: PostModel = Body(...)):
    post = jsonable_encoder(post)
    new_post = await database["posts"].insert_one(post)
    created_post = await database["posts"].find_one({"_id": new_post.inserted_id})
    return created_post


@app.get("/posts/", response_model=List[PostModel])
async def get_posts():
    posts = await database["posts"].find().to_list(50)
    return posts


@app.get("/posts/{slug}", response_model=PostModel)
async def get_post(slug: str):
    post = await database["posts"].find_one({"slug": slug})
    if post is not None:
        return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post not found")


@app.put("/posts/{id}")
async def update_post(id: str, post: UpdatedPostModel = Body(...)):
    post = {key: value for key, value in post.dict().items()
            if value is not None}
    if len(post) >= 1:
        update_result = await database["posts"].update_one({"_id": id}, {"$set": post})
        if update_result.modified_count == 1:
            updated_post = await database["posts"].find_one({"_id": id})
            if update_post is not None:
                return update_post
    existing_post = await database["posts"].find_one({"_id": id})
    if existing_post is not None:
        return existing_post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post not found")


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: str):
    delete_result = await database["posts"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post not found")
