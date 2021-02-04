from abc import ABC, abstractmethod

from services.storage_service import StorageService
from utils.rabbitmq import ConsumerMessageQueue


class IBasePlatform(ABC):
    def __init__(self):
        self.storage_service = StorageService()
        self.message_queue_dep = ConsumerMessageQueue()

    @abstractmethod
    def platform_name(self):
        pass

    @abstractmethod
    def build_platform_users_object(self, users_phones):
        pass

    @abstractmethod
    def notify(self, notification):
        pass

    @abstractmethod
    def platform_response(self, exception, payload):
        pass
