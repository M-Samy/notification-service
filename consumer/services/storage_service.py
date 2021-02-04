from consumer_repositories.FailureRepository import FailureRepository
from consumer_repositories.GroupRepository import GroupRepository
from consumer_repositories.UserRepository import UserRepository


class StorageService:

    def __init__(self):
        self.group_repository = GroupRepository()
        self.user_repository = UserRepository()
        self.failure_repository = FailureRepository()

    def insert_failure(self, doc_data):
        return self.failure_repository.create(failure_payload=doc_data)

    def get_users(self, group_id=None, user_id=None):
        users_phones_list = []
        if group_id:
            users_phones_list = self.group_repository.find_users_by_group_id(group_id=group_id)
        elif user_id:
            users_phones_list.append(user_id)
        return users_phones_list

    def get_users_devices_tokens(self, list_users_phones):
        return self.user_repository.get_devices_tokens(list_users=list_users_phones)
