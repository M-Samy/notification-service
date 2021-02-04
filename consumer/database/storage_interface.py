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
    def insert(self, doc_data, collection):
        pass

    @abstractmethod
    def get_users_by_group_id(self, value, criteria, collection):
        pass

    @abstractmethod
    def get_devices_tokens(self, list_users, collection):
        pass
