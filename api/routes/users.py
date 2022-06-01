from fastapi import APIRouter, HTTPException, Request, Body, status
from fastapi.encoders import jsonable_encoder
from models.User import UserModel, UserOutModel
from utils import hash, verify

router = APIRouter(
    tags=["Users"],
    prefix="/users"
)


@router.put("/{id}")
async def update_user(request: Request, id: str):
    print(request.user)


@router.delete("/id")
async def delete_user(request: Request, id: str):
    pass
