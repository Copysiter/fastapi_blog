from fastapi.security import OAuth2PasswordBearer

oauth2_schemes = OAuth2PasswordBearer(tokenUrl="/login")