from pydantic import BaseModel, validator
from typing import Optional


class NotificationDataModel(BaseModel):
    title: Optional[str]
    body: Optional[str]
    user: Optional[str]
    group_id: Optional[str]
    provider: Optional[str]

    @validator('group_id')
    def check_group_id_or_user(cls, v, values):
        if (not values.get("user")) and (not v):
            raise ValueError('Either group_id or user is required')
        return v

    @validator("title", "body", "provider")
    def validate_not_empty(cls, v):
        if not v:
            raise ValueError('Invalid title or body or provider all fields required')
        return v
