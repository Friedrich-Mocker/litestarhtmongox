from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://root:example@localhost:27017"
client = AsyncIOMotorClient(MONGO_URL)
db = client.item_database
collection = db.items


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
