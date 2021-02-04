from utils.config import get_settings

settings = get_settings()


class RetryConsumer:

    @staticmethod
    def register_queue(channel):
        '''
            Retrying consumer registered here just a temp place used to save retries attempts for failed jobs,
            after the TTL "Time To Live" the failed jobs redirect again for the main exchange to be consumed.
        '''
        channel.exchange_declare(
            exchange=settings.NOTIFICATION_EXCHANGE_NAME,
            exchange_type=settings.NOTIFICATION_EXCHANGE_TYPE
        )

        args = {
            'x-dead-letter-exchange': settings.NOTIFICATION_EXCHANGE_NAME,
            'x-message-ttl': int(settings.NOTIFICATION_TIME_TO_LIVE),
            'x-dead-letter-routing-key': settings.NOTIFICATION_EXCHANGE_TYPE,
        }

        channel.queue_declare(
            queue=settings.RETRY_NOTIFICATION_QUEUE_NAME,
            arguments=args,
            durable=True
        )

        channel.queue_bind(
            exchange=settings.NOTIFICATION_EXCHANGE_NAME,
            queue=settings.RETRY_NOTIFICATION_QUEUE_NAME,
            routing_key=settings.RETRY_NOTIFICATION_EXCHANGE_ROUTING_KEY
        )

        return channel
