from database.mongo_storage import MongoDBStorage


class StorageContext:
    def storage_adapter(self, storage_name):
        if storage_name == "MongoDB":
            return MongoDBStorage().connect()
        else:
            return None
