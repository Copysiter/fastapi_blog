from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from database import Database
from routes import auth, categories, users, posts
from config import settings

app = FastAPI()

app.include_router(
    router=auth.router
)
app.include_router(
    router=users.router
)
app.include_router(
    router=posts.router
)

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

try:
    app.database = Database("blog")
    app.database.login()
except KeyError:
    raise KeyError("Invalid connection url specified.")


if __name__ == "__main__":
    uvicorn.run(
        settings.APP_NAME,
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD
    )
