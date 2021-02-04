from fastapi import Response, APIRouter
from models.users.request.bulk_create import UserBulkDataModel
from repositories.UserRepository import UserRepository
import json
from utils.config import get_settings

settings = get_settings()

router = APIRouter()


@router.post('/users')
def create(users: UserBulkDataModel):
    user_repository = UserRepository(storage_adapter=settings.MONGO_ADAPTER_NAME)
    result = user_repository.bulk_create(users).get_response()
    return Response(json.dumps(result["data"]), result["status_code"])
