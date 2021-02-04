import unittest

from database.mongo_storage import MongoDBStorage
from database.storage_context import StorageContext


class TestGetStorageAdapter(unittest.TestCase):
    def setUp(self):
        self.storage_context = StorageContext()
        self.supported_adapter_name = "MongoDB"
        self.database_name = "notification-service"
        self.un_supported_adapter_name = "Un supported"

    def test_get_storage_adapter(self):
        supported_adapter = self.storage_context.storage_adapter(storage_name=self.supported_adapter_name)
        self.assertIsInstance(supported_adapter, MongoDBStorage)

    def test_un_supported_storage_adapter(self):
        un_supported_adapter = self.storage_context.storage_adapter(storage_name=self.un_supported_adapter_name)
        self.assertIsNone(un_supported_adapter)

    def test_success_connect_with_storage_adapter(self):
        success_connect = self.storage_context.storage_adapter(storage_name=self.supported_adapter_name).connect()
        self.assertIsInstance(success_connect, MongoDBStorage)
        self.assertEqual(success_connect.database.name, self.database_name)


if __name__ == "__main__":
    unittest.main()
