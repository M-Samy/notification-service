from platforms.FCM import FCM
from platforms.Twilio import Twilio
from utils.config import get_settings

settings = get_settings()


class PlatformFactory:
    @staticmethod
    def platform(platform_name):
        if platform_name == settings.FCM_PLATFORM_NAME:
            return FCM()
        elif platform_name == settings.TWILIO_PLATFORM_NAME:
            return Twilio()
