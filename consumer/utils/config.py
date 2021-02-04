from pydantic import BaseSettings
from functools import lru_cache
from utils import config


class ConsumerSettings(BaseSettings):
    class Config:
        env_file = ".env"

    # RabbitMQ
    BROKER_HOST: str
    BROKER_USERNAME: str
    BROKER_PASSWORD: str
    BROKER_PORT: str
    BROKER_VHOST: str

    # Mongodb
    MONGO_HOST: str
    MONGO_PORT: str
    MONGO_USERNAME: str
    MONGO_PASSWORD: str
    MONGO_ADAPTER_NAME: str

    # Database
    USERS_COLLECTION_NAME: str
    NOTIFICATIONS_COLLECTION_NAME: str
    GROUPS_COLLECTION_NAME: str
    FAILURES_COLLECTION_NAME: str

    # Notification Messaging Config
    NOTIFICATION_QUEUE_NAME: str
    NOTIFICATION_EXCHANGE_NAME: str
    NOTIFICATION_EXCHANGE_TYPE: str
    NOTIFICATION_EXCHANGE_ROUTING_KEY: str
    RETRY_NOTIFICATION_QUEUE_NAME: str
    RETRY_NOTIFICATION_EXCHANGE_ROUTING_KEY: str
    NOTIFICATION_TIME_TO_LIVE: str
    NOTIFICATION_SENDING_MAX_TRIES: int

    # FCM Integration
    FCM_PLATFORM_NAME: str
    FCM_APPLICATION_KEY: str

    # Twilio Integration
    TWILIO_ACCOUNT_ID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_NUM_FROM: str
    TWILIO_PLATFORM_NAME: str

    # TEST Environment Variables

    Test_BROKER_HOST: str
    Test_BROKER_USERNAME: str
    Test_BROKER_PASSWORD: str
    Test_BROKER_PORT: str
    Test_BROKER_VHOST: str

    Test_MONGO_HOST: str
    Test_MONGO_PORT: str
    Test_MONGO_USERNAME: str
    Test_MONGO_PASSWORD: str
    Test_MONGO_ADAPTER_NAME: str

    Test_USERS_COLLECTION_NAME: str
    Test_NOTIFICATIONS_COLLECTION_NAME: str
    Test_GROUPS_COLLECTION_NAME: str
    TEST_FAILURES_COLLECTION_NAME: str


class SettingsPerEnvironment(BaseSettings):
    ENV: str = "dev"


@lru_cache()
def get_settings():
    return config.ConsumerSettings()
