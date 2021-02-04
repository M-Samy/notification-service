from database.mongo_storage import MongoDBStorage
from utils.config import get_settings

settings = get_settings()


class GroupRepository:
    def __init__(self):
        self.storage_adapter = MongoDBStorage().connect()

    def find_users_by_group_id(self, group_id):
        return self.storage_adapter.get_users_by_group_id(group_id=group_id, collection=settings.GROUPS_COLLECTION_NAME)
