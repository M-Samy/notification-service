from pydantic import BaseSettings
from functools import lru_cache
from utils import config


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    MONGO_HOST: str
    MONGO_PORT: str
    MONGO_USERNAME: str
    MONGO_PASSWORD: str
    MONGO_ADAPTER_NAME: str

    USERS_COLLECTION_NAME: str
    NOTIFICATIONS_COLLECTION_NAME: str
    GROUPS_COLLECTION_NAME: str

    BROKER_HOST: str
    BROKER_USERNAME: str
    BROKER_PASSWORD: str
    BROKER_PORT: str
    BROKER_VHOST: str

    NOTIFICATION_EXCHANGE_NAME: str
    NOTIFICATION_EXCHANGE_TYPE: str
    NOTIFICATION_EXCHANGE_ROUTING_KEY: str

    # TEST Enviroment Variables

    Test_MONGO_HOST: str
    Test_MONGO_PORT: str
    Test_MONGO_USERNAME: str
    Test_MONGO_PASSWORD: str
    Test_MONGO_ADAPTER_NAME: str

    Test_USERS_COLLECTION_NAME: str
    Test_NOTIFICATIONS_COLLECTION_NAME: str
    Test_GROUPS_COLLECTION_NAME: str

    Test_BROKER_HOST: str
    Test_BROKER_USERNAME: str
    Test_BROKER_PASSWORD: str
    Test_BROKER_PORT: str
    Test_BROKER_VHOST: str

    Test_NOTIFICATION_EXCHANGE_NAME: str
    Test_NOTIFICATION_EXCHANGE_TYPE: str
    Test_NOTIFICATION_EXCHANGE_ROUTING_KEY: str


@lru_cache()
def get_settings():
    return config.Settings()
