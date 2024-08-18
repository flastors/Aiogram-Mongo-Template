from bson.objectid import ObjectId as BsonObjectId
from motor.motor_tornado import MotorCollection
from pydantic import BaseModel
from typing import Dict, Any

from loader import db


class ObjectId(BsonObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, BsonObjectId):
            raise TypeError('ObjectId required')
        return str(v)


class Base(BaseModel):
    _collection: MotorCollection = None

    @classmethod
    async def count(cls, filter: Dict[str, Any] = dict()):
        num = await cls._collection.count_documents(filter)
        return num

    @classmethod
    async def get(cls, id: int):
        obj = await cls._collection.find_one({'_id': id})
        return cls(**obj) if obj else None
    
    @classmethod
    async def get_field(cls, fields: Dict[str, Any] = dict()):
        obj = await cls._collection.find_one(fields)
        return cls(**obj) if obj else None

    @classmethod
    async def get_all(cls):
        objs = cls._collection.find()
        return [cls(**u) async for u in objs]
    
    @classmethod
    async def get_all_field(cls, field: Dict[str, Any] = dict()):
        objs = cls._collection.find(field)
        return [cls(**u) async for u in objs]        

    @classmethod
    async def update(cls, id: int, **kwargs):
        await cls._collection.find_one_and_update({'_id': id}, {'$set': kwargs})
        return await cls.get(id)

    @classmethod
    async def create(cls, **kwargs):
        if '_id' not in kwargs:
            kwargs["_id"] = await cls.count() + 1
        obj = cls(**kwargs)
        obj = await cls._collection.insert_one(obj.model_dump(by_alias=True))
        return await cls.get(obj.inserted_id)

    @classmethod
    async def delete(cls, id: int):
        await cls._collection.find_one_and_delete({'_id': id})
        return True

    @classmethod
    def set_collection(cls, collection: str):
        cls._collection = db[collection]
