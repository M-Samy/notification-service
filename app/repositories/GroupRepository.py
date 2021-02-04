from exceptions.ExceptionFactory import ExceptionFactory
from exceptions.FailedConnectionException import FailedConnection
from repositories.BaseRepository import IBaseRepository
from repositories.UserRepository import UserRepository
from utils.config import get_settings
from utils.response import ObjectResponse

settings = get_settings()


class GroupRepository(IBaseRepository):

    def __init__(self, storage_adapter):
        super().__init__(storage_name=storage_adapter)
        self.user_repository_dep = UserRepository(storage_adapter=storage_adapter, storage_context=self.storage_context)

    def create(self, group_instance, *args, **kwargs):
        result = ObjectResponse()
        if not self.storage_adapter:
            result.cls_exception = ExceptionFactory.get_exception(
                FailedConnection,
                503,
                "Failed to get storage adapter")
            return result

        group_data = self.get_instance_dict(group_instance)
        response = self.user_repository_dep.bulk_create(users=group_data)
        group_data["users"] = response.users_phones
        group = self.storage_adapter.insert(doc_data=group_data, collection=settings.GROUPS_COLLECTION_NAME)
        result.response = {
            'data': {
                'status': True,
                'group_id': str(group.inserted_id)
            },
            'status_code': 201
        }
        return result

    def bulk_create(self, *args, **kwargs):
        pass
