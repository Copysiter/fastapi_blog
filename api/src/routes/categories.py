from typing import List
from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.models import PostModel, UpdatedPostModel

router = APIRouter()


@router.get("/{category}", response_model=List[PostModel])
async def get_category(request: Request, category: str):
    posts = await request.app.database["posts"].find({"category": category}).to_list(50)
    return posts
