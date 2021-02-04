from fastapi import Response, APIRouter
from models.groups.request.create import CreateGroupModel
from repositories.GroupRepository import GroupRepository
import json
from utils.config import get_settings

settings = get_settings()

router = APIRouter()


@router.post('/groups')
def create(group: CreateGroupModel):
    group_repository = GroupRepository(storage_adapter=settings.MONGO_ADAPTER_NAME)
    result = group_repository.create(group).get_response()
    return Response(json.dumps(result["data"]), result["status_code"])
