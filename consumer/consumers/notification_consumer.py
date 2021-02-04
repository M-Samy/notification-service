from services.notify_service import NotifyService
from utils.config import get_settings

settings = get_settings()


class NotificationConsumer:

    @staticmethod
    def register_queue(channel):
        channel.exchange_declare(
            exchange=settings.NOTIFICATION_EXCHANGE_NAME,
            exchange_type=settings.NOTIFICATION_EXCHANGE_TYPE
        )

        channel.queue_declare(
            queue=settings.NOTIFICATION_QUEUE_NAME,
            durable=True
        )

        channel.queue_bind(
            exchange=settings.NOTIFICATION_EXCHANGE_NAME,
            queue=settings.NOTIFICATION_QUEUE_NAME,
            routing_key=settings.NOTIFICATION_EXCHANGE_ROUTING_KEY
        )

        channel.basic_consume(
            queue=settings.NOTIFICATION_QUEUE_NAME,
            on_message_callback=NotifyService.notify,
            auto_ack=True
        )

        return channel
