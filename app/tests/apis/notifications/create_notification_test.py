import unittest
from models.notifications.request.create import NotificationDataModel
from repositories.NotificationRepository import NotificationRepository


class TestCreateNotificationRequest(unittest.TestCase):
    def setUp(self):
        self.success_fake_notification = NotificationDataModel(
            title="Test Notification Title",
            body="Test Notification Body",
            user="+201111111111",
            group_id="",
            provider="FCM"
        )
        self.notification_repository = None
        self.adapter_name = "MongoDB"

    def test_success_create_notification(self):
        self.notification_repository = NotificationRepository(storage_adapter=self.adapter_name)
        result = self.notification_repository.create(
            notification_instance=self.success_fake_notification).get_response()
        self.assertTrue(result['data']["created"])
        self.assertEqual(result["status_code"], 201)


if __name__ == "__main__":
    unittest.main()
