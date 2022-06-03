from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta
from models.Token import TokenData
from config import settings

oauth2_schemes = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    try:
        encoded_jwt: str = jwt.encode(
            to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError as error:
        raise JWTError(error)
    return encoded_jwt


def verify_access_token(token: str, credentials_exception) -> TokenData:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, [settings.ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=id)
    except JWTError:
        raise credentials_exception

    return token_data


async def get_current_user(request: Request, token: str = Depends(oauth2_schemes)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    token_data: TokenData = verify_access_token(token, credentials_exception)
    user = await request.app.database.get_user({"_id": token_data.id})
    return user
