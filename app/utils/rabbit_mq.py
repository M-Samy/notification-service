import pika
from utils.config import get_settings

settings = get_settings()


class MessageQueue(object):
    def __init__(self):
        connection = pika.PlainCredentials(settings.BROKER_USERNAME, settings.BROKER_PASSWORD)
        params = pika.ConnectionParameters(
            host=settings.BROKER_HOST,
            port=settings.BROKER_PORT,
            virtual_host=settings.BROKER_VHOST,
            credentials=connection
        )
        self.conn = pika.BlockingConnection(parameters=params)
        self.channel = self.conn.channel()

    def create_exchange(self, exchange_name, exchange_type):
        self.channel.exchange_declare(
            exchange=exchange_name,
            exchange_type=exchange_type
        )

    def send(self, message):
        self.create_exchange(
            exchange_name=settings.NOTIFICATION_EXCHANGE_NAME,
            exchange_type=settings.NOTIFICATION_EXCHANGE_TYPE
        )
        self.channel.basic_publish(
            exchange=settings.NOTIFICATION_EXCHANGE_NAME,
            routing_key=settings.NOTIFICATION_EXCHANGE_ROUTING_KEY,
            body=message
        )
