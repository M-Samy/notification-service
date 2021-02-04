import unittest
from platforms.FCM import FCM
from platforms.PlatformFactory import PlatformFactory
from platforms.Twilio import Twilio


class TestGetNotificationPlatform(unittest.TestCase):
    def setUp(self):
        self.fcm_platform_name = "FCM"
        self.twilio_platform_name = "SMS"
        self.platform_factory = PlatformFactory()

    def test_get_fcm_platform(self):
        fcm_platform = self.platform_factory.platform(platform_name=self.fcm_platform_name)
        self.assertIsInstance(fcm_platform, FCM)

    def test_get_twilio_platform(self):
        twilio_platform = self.platform_factory.platform(platform_name=self.twilio_platform_name)
        self.assertIsInstance(twilio_platform, Twilio)


if __name__ == "__main__":
    unittest.main()
