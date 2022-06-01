from fastapi import APIRouter, Body, Depends, Request
from oauth2 import oauth2_schemes
from models.Post import PostModel
router = APIRouter(
    tags=["Posts"],
    prefix="/posts"
)


@router.post("/")
async def publish_post(request: Request, post: PostModel = Body(...), current_user=Depends(oauth2_schemes)):
    print(current_user)
