import pika
from consumers.notification_consumer import NotificationConsumer
from consumers.retrying_consumer import RetryConsumer
from utils.config import get_settings

settings = get_settings()


def start():
    while True:
        connection = pika.PlainCredentials(settings.BROKER_USERNAME, settings.BROKER_PASSWORD)
        params = pika.ConnectionParameters(
            host=settings.BROKER_HOST,
            port=settings.BROKER_PORT,
            virtual_host=settings.BROKER_VHOST,
            credentials=connection
        )
        connection = pika.BlockingConnection(parameters=params)
        channel = connection.channel()

        # Register consumer to consumer notifications messages.
        channel = NotificationConsumer.register_queue(channel)

        # Register new consumer for retrying sending notifications.
        channel = RetryConsumer.register_queue(channel)
        channel.start_consuming()


if __name__ == "__main__":
    start()
