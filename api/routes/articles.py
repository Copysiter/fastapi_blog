from typing import List
from fastapi import APIRouter, Body, HTTPException, Request, Response, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models import PostModel, UpdatedPostModel

router = APIRouter(
    tags=["articles"],
    prefix="/articles"
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def publish_article(request: Request, article: PostModel = Body(...)):
    article = jsonable_encoder(article)
    new_article = await request.app.database.insert("articles", article)
    created_article = await request.app.database.find_article_by_id(new_article.inserted_id)
    return created_article


@router.get("/", response_model=List[PostModel])
async def get_posts(request: Request):
    posts = await request.app.database.find_all("articles")
    return posts


@router.put("/{id}")
async def update_post(request: Request, id: str, post: UpdatedPostModel = Body(...)):
    post = {key: value for key, value in post.dict().items()
            if value is not None}
    if len(post) >= 1:
        update_result = await request.app.database["posts"].update_one({"_id": id}, {"$set": post})
        if update_result.modified_count == 1:
            updated_post = await request.app.database["posts"].find_one({"_id": id})
            if updated_post is not None:
                return updated_post
    existing_post = await request.app.database["posts"].find_one({"_id": id})
    if existing_post is not None:
        return existing_post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post not found")


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(request: Request, id: str):
    delete_result = await request.app.database["posts"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post not found")
