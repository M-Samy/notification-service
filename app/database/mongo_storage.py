from database.storage_interface import StorageInterface
from utils.config import get_settings
from pymongo import MongoClient

settings = get_settings()


class MongoDBStorage(StorageInterface):

    def get_storage_name(self):
        return settings.MONGO_ADAPTER_NAME

    def connect(self):
        if settings.MONGO_USERNAME and settings.MONGO_PASSWORD:
            uri = f"mongodb://{settings.MONGO_USERNAME}:{settings.MONGO_PASSWORD}@{settings.MONGO_HOST}:{settings.MONGO_PORT}"
        else:
            uri = f"mongodb://{settings.MONGO_HOST}:{settings.MONGO_PORT}"

        self.adapter_connection = MongoClient(uri)
        self.database = self.adapter_connection["notification-service"]
        return self

    def insert(self, doc_data, collection):
        self.collection = self.database[collection]
        return self.collection.insert_one(document=doc_data)

    def update(self, filters, doc_data, collection):
        self.collection = self.database[collection]
        return self.collection.update_one(
            filters,
            {"$set": doc_data}
        )

    def bulk_insert(self, docs, collection):
        self.collection = self.database[collection]
        return self.collection.insert_many(documents=docs)

    def find_with_list_ids(self, list_ids=None, criteria="_id", collection=None):
        self.collection = self.database[collection]
        docs = list(self.collection.aggregate([{"$match": {criteria: {"$in": list_ids}}}]))
        return [str(doc[criteria]) for doc in docs]
