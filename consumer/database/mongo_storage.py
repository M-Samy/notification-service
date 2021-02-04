from database.storage_interface import StorageInterface
from utils.config import get_settings
from pymongo import MongoClient
from bson.objectid import ObjectId

settings = get_settings()


class MongoDBStorage(StorageInterface):

    def connect(self):
        if settings.MONGO_USERNAME and settings.MONGO_PASSWORD:
            uri = f"mongodb://{settings.MONGO_USERNAME}:{settings.MONGO_PASSWORD}@{settings.MONGO_HOST}:{settings.MONGO_PORT}"
        else:
            uri = f"mongodb://{settings.MONGO_HOST}:{settings.MONGO_PORT}"

        self.adapter_connection = MongoClient(uri)
        self.database = self.adapter_connection["notification-service"]
        return self

    def insert(self, doc_data=None, collection=None):
        self.collection = self.database[collection]
        instance = self.collection.insert_one(document=doc_data)
        return instance

    def get_users_by_group_id(self, group_id=None, criteria="_id", collection=None):
        self.collection = self.database[collection]
        group_id = ObjectId(group_id)
        group = self.collection.find_one(filter={"_id": group_id})
        return group.get("users")

    def get_devices_tokens(self, list_users, collection=None):
        self.collection = self.database[collection]

        pipeline = [
            {'$match': {'phone': {'$exists': True, "$in": list_users},
                        'fcm_token': {'$exists': True, "$not": {"$size": 0}, "$ne": ""}}}
        ]

        docs = list(self.collection.aggregate(pipeline))
        return list(map(lambda doc: str(doc.get("fcm_token")), docs))
