from fastapi import APIRouter, Depends, HTTPException, Request, Body, status
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from models.User import UserModel, UserOutModel
from utils import hash, verify

router = APIRouter(
    tags=["Authentication"],
)


@router.post("/register", response_model=UserOutModel)
async def register(request: Request, user: UserModel = Body(...)):
    try:
        hashed_password = hash(user.password)
        user.password = hashed_password
        user = jsonable_encoder(user)
        new_user = await request.app.database.insert("users", user)
        created_user = await request.app.database.get_user({"_id": new_user.inserted_id})
        return created_user
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.post("/login", response_model=UserOutModel)
async def login(request: Request, user_credentials: OAuth2PasswordRequestForm = Depends()):
    try:
        user = await request.app.database.get_user({"username": user_credentials.username})
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid username !"
            )
        valid_password = verify(
            user_credentials.password, user["password"])
        if not valid_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid password"
            )
        return user
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
