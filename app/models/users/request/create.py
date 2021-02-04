from pydantic import BaseModel


class UserDataModel(BaseModel):
    name: str
    phone: str
    fcm_token: str
