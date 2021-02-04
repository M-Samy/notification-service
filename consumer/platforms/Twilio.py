from paltforms_exceptions import TwilioExceptionsCodes
from platforms.BasePlatform import IBasePlatform
from twilio.rest import Client
from services.storage_service import StorageService
from utils.config import get_settings

settings = get_settings()


class Twilio(IBasePlatform):
    def __init__(self):
        super().__init__()
        self.client = Client(
            username=settings.TWILIO_ACCOUNT_ID,
            password=settings.TWILIO_AUTH_TOKEN
        )

    def platform_name(self):
        return settings.TWILIO_PLATFORM_NAME

    def build_platform_users_object(self, users_phones_list):
        return users_phones_list

    def notify(self, notification_payload):
        message_body = notification_payload.get("body", "")
        users_phones = [user_phone for user_phone in notification_payload.get("users", [])]
        if users_phones:
            return self.fire_notifications(phones=users_phones, message=message_body, payload=notification_payload)
        else:
            print("No phones existed")
            return False

    def fire_notifications(self, phones, message, payload):
        result = None
        try:
            for phone in phones:
                result = self.client.messages.create(
                    to=phone,
                    from_=settings.TWILIO_NUM_FROM,
                    body=message
                )

        except Exception as exception:
            print("Exception occurred during send notification through {} due to {}".
                  format(self.platform_name(), exception.__repr__()))
            self.platform_response(exception=exception, notification_payload=payload)
        return result

    def platform_response(self, exception, notification_payload):
        """
            ## Trying to fix rate-limit or service down by retrying.
            ## After max of retries are exceeded we will log the payload
        """
        exception_code = exception.code
        exception_message = exception.msg

        remaining_retries = \
            notification_payload.get("remaining_retries", settings.NOTIFICATION_SENDING_MAX_TRIES + 1) - 1
        logged = notification_payload.get("logged", False)

        if exception_code in TwilioExceptionsCodes.RATE_LIMIT_LIST_CODES_EXCEPTION and remaining_retries > 0:
            self.message_queue_dep.send(message=notification_payload)
        elif not logged:
            notification_payload.update({
                "exception_code": exception_code,
                "exception_message": exception_message,
                "logged": True
            })
            notification_payload.pop("_id", None)
            storage_service = StorageService()
            storage_service.insert_failure(doc_data=notification_payload)
