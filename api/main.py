from fastapi import FastAPI
import motor.motor_asyncio
import os
from dotenv import load_dotenv
import uvicorn
from src.router import router as posts_router
load_dotenv()

app = FastAPI()
app.include_router(router=posts_router, prefix="/posts")


@app.on_event("startup")
async def start_database():
    app.database_client = motor.motor_asyncio.AsyncIOMotorClient(
        os.environ["MONGODB_URL"])
    app.database = app.database_client.blog


@app.on_event("shutdown")
async def shutdown_database():
    app.database_client.close()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )