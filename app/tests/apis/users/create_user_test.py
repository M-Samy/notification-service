import unittest
from models.users.request.bulk_create import UserBulkDataModel
from models.users.request.create import UserDataModel
from repositories.UserRepository import UserRepository


class TestCreateUserRequest(unittest.TestCase):
    def setUp(self):
        self.fake_users = UserBulkDataModel(
            users=[
                UserDataModel(
                    name="Test Users 1",
                    phone="+201111111111",
                    fcm_token=""
                ),
                UserDataModel(
                    name="Test Users 2",
                    phone="+202222222222",
                    fcm_token=""
                ),
            ]
        )
        self.user_repository = None
        self.adapter_name = "MongoDB"

    def test_create_user(self):
        self.user_repository = UserRepository(storage_adapter=self.adapter_name)
        result = self.user_repository.bulk_create(users=self.fake_users).get_response()
        self.assertTrue(result['data']["status"])
        self.assertEqual(result["status_code"], 201)
        data = {
            'status': True,
            'users_phones': ['+201111111111', '+202222222222']
        }
        self.assertDictEqual(result['data'], data)


if __name__ == "__main__":
    unittest.main()
