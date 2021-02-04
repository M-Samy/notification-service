import unittest
from platforms.FCM import FCM
from platforms.Twilio import Twilio
from services.notify_service import NotifyService


class TestConsumingNotificationsRequest(unittest.TestCase):
    def setUp(self):
        self.notification_payload = {
            'title': 'Example notification title',
            'body': 'Example notification body',
            'user': '+201111111111',
            'group_id': '',
            'provider': 'FCM',
            '_id': 'USER DB STRING OBJECT_ID',
            'users': ['GENERATED TOKEN BY FCM']
        }
        self.twilio_notification_payload = {
            'title': 'Example notification title',
            'body': 'Example notification body',
            'user': '+201111111111',
            'group_id': '',
            'provider': 'SMS',
            '_id': 'USER DB STRING OBJECT_ID',
            'users': ['GENERATED TOKEN BY FCM']
        }

        self.notify_service = NotifyService()
        self.fcm_platform = FCM()
        self.twilio_platform = Twilio()

    def test_consuming_fcm_notification_payload(self):
        '''
            This test case will be failed cause we haven't fcm token for user.
        '''
        notify_status = self.fcm_platform.notify(
            notification_payload=self.notification_payload
        )
        self.assertIsNone(notify_status["topic_message_id"])
        self.assertEqual(notify_status["failure"], 1)
        self.assertEqual(notify_status["success"], 0)

    def test_consuming_twilio_notification_payload(self):
        notify_status = self.twilio_platform.notify(
            notification_payload=self.twilio_notification_payload
        )
        self.assertIsNone(notify_status)


if __name__ == "__main__":
    unittest.main()
