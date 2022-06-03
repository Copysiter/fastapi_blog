from typing import Optional
from fastapi import APIRouter, Body, Depends, Request
from fastapi.encoders import jsonable_encoder
from models.Post import PostModel
from oauth2 import get_current_user

router = APIRouter(
    tags=["Posts"],
    prefix="/posts"
)


@router.post("/")
async def publish_post(request: Request, post: PostModel = Body(...), current_user: str = Depends(get_current_user)):
    post = jsonable_encoder(post)
    new_post = await request.app.database.insert("posts", post)
    created_post = await request.app.database.find_post(new_post.inserted_id)
    return created_post


@router.get("/")
async def get_posts(request: Request, limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # posts = await request.app.database.find_all("posts", limit, skip)
    posts = await request.app.database.find_all("posts", limit, skip, search)
    return posts


@router.put("/{id}")
async def update_post(request: Request, id: str, post=Body(...), current_id=Depends(get_current_user)):
    pass


@router.delete("/{id}")
async def delete_post(request: Request, id: str, post=Body(...), current_id=Depends(get_current_user)):
    pass
