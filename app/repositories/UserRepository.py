from exceptions import ExceptionFactory
from exceptions.FailedConnectionException import FailedConnection
from exceptions.ExceptionFactory import ExceptionFactory
from repositories.BaseRepository import IBaseRepository
from utils.config import get_settings
from utils.response import ObjectResponse

settings = get_settings()


class UserRepository(IBaseRepository):
    def __init__(self, storage_adapter, storage_context=None):
        super().__init__(storage_adapter, storage_context)

    def create(self, user_data):
        return self.storage_adapter.insert(
            doc_data=user_data,
            collection=settings.USERS_COLLECTION_NAME
        )

    def update(self, new_data, filters):
        result = ObjectResponse()
        if not self.storage_adapter:
            result.cls_exception = ExceptionFactory.get_exception(
                FailedConnection,
                503,
                "Failed to get storage adapter")
            return result

        response = self.storage_adapter.update(
            filters=filters,
            doc_data=new_data,
            collection=settings.USERS_COLLECTION_NAME
        )

        if response.raw_result.get("updatedExisting"):
            message = "User updated successfully"
        else:
            message = "Failed to update user might be not exist"

        result.status = True
        result.response = {
            'data': {
                'updated': response.raw_result.get("updatedExisting"),
                'message': message
            },
            'status_code': 200
        }
        return result

    def bulk_create(self, users):
        result = ObjectResponse()
        if not self.storage_adapter:
            result.cls_exception = ExceptionFactory.get_exception(
                FailedConnection,
                503,
                "Failed to get storage adapter")
            return result

        users_data = self.get_instance_dict(users)
        users_data = users_data.get("users")
        users_phones = self.insert_only_new_users_return_ids(
            users_list=users_data
        )
        result.users_phones = users_phones
        result.response = {
            'data': {
                "status": True,
                "users_phones": users_phones
            },
            'status_code': 201
        }
        return result

    def insert_only_new_users_return_ids(self, users_list):
        inserted_list = []
        numbers_list = list(map(lambda user: user.get("phone"), users_list))
        found_users = self.find(
            numbers_list=numbers_list,
            criteria="phone"
        )
        for index, val in enumerate(users_list):
            if val["phone"] not in found_users:
                inserted_list.append(val)

        if inserted_list:
            self.storage_adapter.bulk_insert(docs=inserted_list, collection=settings.USERS_COLLECTION_NAME)
        return numbers_list

    def find(self, numbers_list, criteria):
        users_list = self.storage_adapter.find_with_list_ids(
            list_ids=numbers_list,
            criteria=criteria,
            collection=settings.USERS_COLLECTION_NAME
        )
        return users_list
