from database.mongo_storage import MongoDBStorage
from utils.config import get_settings

settings = get_settings()


class FailureRepository:
    def __init__(self):
        self.storage_adapter = MongoDBStorage().connect()

    def create(self, failure_payload):
        return self.storage_adapter.insert(doc_data=failure_payload, collection=settings.FAILURES_COLLECTION_NAME)
