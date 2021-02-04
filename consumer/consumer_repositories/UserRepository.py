from database.mongo_storage import MongoDBStorage
from utils.config import get_settings

settings = get_settings()


class UserRepository:
    def __init__(self):
        self.storage_adapter = MongoDBStorage().connect()

    def get_devices_tokens(self, list_users):
        return self.storage_adapter.get_devices_tokens(list_users=list_users, collection=settings.USERS_COLLECTION_NAME)
