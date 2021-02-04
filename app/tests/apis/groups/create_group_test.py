import unittest
from models.groups.request.create import CreateGroupModel
from models.users.request.create import UserDataModel
from repositories.GroupRepository import GroupRepository


class TestCreateGroupRequest(unittest.TestCase):
    def setUp(self):
        self.fake_group = CreateGroupModel(
            name="Test Group",
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
        self.group_repository = None
        self.adapter_name = "MongoDB"

    def test_create_group(self):
        self.group_repository = GroupRepository(storage_adapter=self.adapter_name)
        result = self.group_repository.create(group_instance=self.fake_group).get_response()
        self.assertTrue(result['data']["status"])
        self.assertEqual(result["status_code"], 201)


if __name__ == "__main__":
    unittest.main()
