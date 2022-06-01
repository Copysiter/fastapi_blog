from bson.objectid import ObjectId
from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="str")


def hash(plain_password: str):
    return password_context.hash(plain_password)


def verify(plain_password: str, password: str) -> bool:
    return password_context.verify(plain_password, password)
