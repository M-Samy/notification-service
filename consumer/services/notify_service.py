import json
from platforms.PlatformFactory import PlatformFactory
from services.storage_service import StorageService


class NotifyService:
    @staticmethod
    def notify(ch, method, pros, data):
        body = json.loads(data.decode("utf-8"))

        group_id = body.get("group_id")
        user_id = body.get("user")
        notification_platform_name = body.get("provider")

        if not notification_platform_name:
            return None

        storage_service = StorageService()
        users_phones = storage_service.get_users(
            group_id=group_id,
            user_id=user_id
        )
        platform_instance = PlatformFactory.platform(platform_name=notification_platform_name)
        users = platform_instance.build_platform_users_object(users_phones_list=users_phones)

        body.update({"users": users})

        return platform_instance.notify(notification_payload=body)
