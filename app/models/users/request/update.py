from pydantic import BaseModel


class UserUpdateDataModel(BaseModel):
    phone: str
    fcm_token: str
