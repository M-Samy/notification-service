from pyfcm import FCMNotification
from platforms.BasePlatform import IBasePlatform
from services.storage_service import StorageService
from utils.config import get_settings

settings = get_settings()


class FCM(IBasePlatform):
    def __init__(self):
        super().__init__()
        self.push_notification_service = FCMNotification(
            api_key=settings.FCM_APPLICATION_KEY
        )

    def platform_name(self):
        return settings.FCM_PLATFORM_NAME

    def build_platform_users_object(self, users_phones_list):
        return self.storage_service.get_users_devices_tokens(list_users_phones=users_phones_list)

    def notify(self, notification_payload):
        devices_tokens_list = notification_payload.get("users", None)
        if devices_tokens_list:
            return self.fire_notifications(
                devices_tokens_list=devices_tokens_list,
                payload=notification_payload
            )
        else:
            # This case only into testing cause we can get only single token from FCM not multiple devices token.
            # So we test only into single user.
            print("No valid devices token existed")
            return False

    def fire_notifications(self, devices_tokens_list, payload):
        result = None
        try:
            title = payload.get("title", "")
            text = payload.get("body", "")

            result = self.push_notification_service.notify_multiple_devices(
                registration_ids=devices_tokens_list,
                message_title=title,
                message_body=text
            )
        except Exception as exception:
            print(">>>>>>> Exception occurred during notify through {} due to {}".
                  format(self.platform_name(), exception.__repr__()))
            self.platform_response(exception=exception, notification_payload=payload)
        return result

    def platform_response(self, exception, notification_payload):
        """
            # TODO check FCM exceptions to differentiate between
                ## Exceptions that we need to log it for monitoring
                ## Exceptions such as rate-limit or service down to retry.
        """
        remaining_retries = \
            notification_payload.get("remaining_retries", settings.NOTIFICATION_SENDING_MAX_TRIES + 1) - 1
        logged = notification_payload.get("logged", False)

        notification_payload.update({
            "exception_message": exception.__repr__(),
            "remaining_retries": remaining_retries,
            "logged": logged
        })

        if remaining_retries == 0:
            notification_payload.pop("_id", None)
            storage_service = StorageService()
            storage_service.insert_failure(doc_data=notification_payload)
            notification_payload.update({"logged": True})

        if remaining_retries > 0:
            self.message_queue_dep.send(message=notification_payload)
