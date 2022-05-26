from typing import List
from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.models import PostModel, UpdatedPostModel

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def publish_post(request: Request, post: PostModel = Body(...)):
    post = jsonable_encoder(post)
    new_post = await request.database["posts"].insert_one(post)
    created_post = await request.database["posts"].find_one({"_id": new_post.inserted_id})
    return created_post


@router.get("/", response_model=List[PostModel])
async def get_posts(request: Request):
    posts = await request.database["posts"].find().to_list(50)
    return posts


@router.get("/{slug}", response_model=PostModel)
async def get_post(request: Request, slug: str):
    post = await request.database["posts"].find_one({"slug": slug})
    if post is not None:
        return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post not found")


@router.put("/{id}")
async def update_post(request: Request, id: str, post: UpdatedPostModel = Body(...)):
    post = {key: value for key, value in post.dict().items()
            if value is not None}
    if len(post) >= 1:
        update_result = await request.database["posts"].update_one({"_id": id}, {"$set": post})
        if update_result.modified_count == 1:
            updated_post = await request.database["posts"].find_one({"_id": id})
            if updated_post is not None:
                return updated_post
    existing_post = await request.database["posts"].find_one({"_id": id})
    if existing_post is not None:
        return existing_post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post not found")


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(request: Request, id: str):
    delete_result = await request.database["posts"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post not found")
