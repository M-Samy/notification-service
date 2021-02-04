from pydantic import BaseModel
from typing import Optional
from typing import List

from models.users.request.create import UserDataModel


class CreateGroupModel(BaseModel):
    name: Optional[str]
    users: Optional[List[UserDataModel]]
