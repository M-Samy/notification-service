import unittest
from repositories.UserRepository import UserRepository


class TestUpdateFCMTokenRequest(unittest.TestCase):
    def setUp(self):
        self.fake_request = {"fcm_token": "FCM TOKEN GENERATED"}
        self.user_repository = None
        self.adapter_name = "MongoDB"

    def test_update_user(self):
        self.user_repository = UserRepository(storage_adapter=self.adapter_name)
        filters = {"phone": "+201111111111"}
        result = self.user_repository.update(new_data=self.fake_request, filters=filters).get_response()
        self.assertTrue(result['data']["updated"])
        self.assertEqual(result["status_code"], 200)


if __name__ == "__main__":
    unittest.main()
