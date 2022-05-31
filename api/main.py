from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import uvicorn
from database import Database
from routes.articles import router as articles_router
load_dotenv()

app = FastAPI()

app.include_router(router=articles_router)

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

try:
    app.database = Database("blog")
    app.database.login()
except KeyError:
    raise KeyError("Invalid connection url specified.")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
