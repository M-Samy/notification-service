from abc import ABC, abstractmethod
from fastapi.encoders import jsonable_encoder
from database.storage_context import StorageContext


class IBaseRepository(ABC):
    def __init__(self, storage_name, storage_context=None):
        self.storage_context = StorageContext() if not storage_context else storage_context
        self.storage_adapter = self.get_storage_adapter(storage_name=storage_name)

    def get_storage_adapter(self, storage_name):
        return self.storage_context.storage_adapter(storage_name=storage_name)

    @staticmethod
    def get_instance_dict(group):
        return jsonable_encoder(group)

    @abstractmethod
    def create(self, *args, **kwargs):
        pass

    @abstractmethod
    def bulk_create(self, *args, **kwargs):
        pass
