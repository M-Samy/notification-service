from abc import ABC, abstractmethod


class StorageInterface(ABC):

    def __init__(self):
        self.database = None
        self.collection = None
        self.adapter_connection = None

    @abstractmethod
    def connect(self, **kwargs):
        pass

    @abstractmethod
    def insert(self, doc, collection):
        pass

    @abstractmethod
    def bulk_insert(self, docs, collection):
        pass

    @abstractmethod
    def get_storage_name(self, **kwargs):
        pass

    @abstractmethod
    def find_with_list_ids(self, list_ids, criteria, collection):
        pass

    @abstractmethod
    def update(self, filters, data, collection):
        pass
