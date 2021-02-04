from fastapi import Response, APIRouter
from models.users.request.update import UserUpdateDataModel
from repositories.UserRepository import UserRepository
import json
from utils.config import get_settings

settings = get_settings()

router = APIRouter()


@router.post('/user/update-fcm-token')
def update_user_fcm_token(user: UserUpdateDataModel):
    user_repository = UserRepository(storage_adapter=settings.MONGO_ADAPTER_NAME)
    new_data = {"fcm_token": user.fcm_token}
    filters = {"phone": user.phone}
    result = user_repository.update(new_data=new_data, filters=filters).get_response()
    return Response(json.dumps(result["data"]), result["status_code"])
