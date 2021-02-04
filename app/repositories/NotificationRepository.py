from exceptions.ExceptionFactory import ExceptionFactory
from exceptions.FailedConnectionException import FailedConnection
from repositories.BaseRepository import IBaseRepository
from utils.config import get_settings
from utils.rabbit_mq import MessageQueue
from utils.response import ObjectResponse
import json

settings = get_settings()


class NotificationRepository(IBaseRepository):

    def __init__(self, storage_adapter):
        super().__init__(storage_name=storage_adapter)
        self.message_queue_dep = MessageQueue()

    def create(self, notification_instance, *args, **kwargs):
        result = ObjectResponse()
        if not self.storage_adapter:
            result.cls_exception = ExceptionFactory.get_exception(
                FailedConnection,
                503,
                "Failed to get storage adapter")
            return result

        notification_data = self.get_instance_dict(notification_instance)
        notification = self.storage_adapter.insert(
            doc_data=notification_data,
            collection=settings.NOTIFICATIONS_COLLECTION_NAME
        )
        result.response = {
            'data': {
                'created': True,
                'published': True,
                'notification_id': str(notification.inserted_id)
            },
            'status_code': 201
        }

        message = self.build_notification_message(
            notification_data=notification_data,
            notification_instance=notification
        )
        self.message_queue_dep.send(message=message)
        return result

    def bulk_create(self, *args, **kwargs):
        pass

    @staticmethod
    def build_notification_message(notification_data, notification_instance):
        notification_data.update(_id=str(notification_instance.inserted_id))
        return json.dumps(notification_data)
