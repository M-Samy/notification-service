from pydantic import BaseModel
from typing import Optional
from typing import List

from models.users.request.create import UserDataModel


class UserBulkDataModel(BaseModel):
    users: Optional[List[UserDataModel]]
