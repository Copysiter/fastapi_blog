from motor.motor_asyncio import AsyncIOMotorClient
from config import settings
from typing import Optional

class Database:
    def __init__(self, database_name: str):
        self.database_name = database_name

    def login(self):
        try:
            client = AsyncIOMotorClient(settings.DATABASE_URL)
        except KeyError:
            raise KeyError
        self.database = client.get_database(self.database_name)

    async def insert(self, collection_name: str, data):
        collection = self.database.get_collection(collection_name)
        insert_result = await collection.insert_one(data)
        return insert_result

    async def find_post(self, id: str):
        collection = self.database.get_collection("posts")
        find_result = await collection.find_one({"_id": id})
        return find_result

    async def get_user(self, query: dict):
        collection = self.database.get_collection("users")
        find_result = await collection.find_one(query)
        return find_result

    async def find_all(self, collection_name: str, max_results: int = 50, skip: int = 0, search: Optional[str] = ""):
        collection = self.database.get_collection(collection_name)
        find_result = await collection.find({"title": {"$regex": search}},
                                            limit=max_results, skip=skip).to_list(max_results)
        return find_result
