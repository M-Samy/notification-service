from fastapi import Response, APIRouter
from models.notifications.request.create import NotificationDataModel
from repositories.NotificationRepository import NotificationRepository
import json
from utils.config import get_settings

settings = get_settings()

router = APIRouter()


@router.post('/notifications')
def create(notification: NotificationDataModel):
    notification_repository = NotificationRepository(storage_adapter=settings.MONGO_ADAPTER_NAME)
    result = notification_repository.create(notification).get_response()
    return Response(json.dumps(result["data"]), result["status_code"])
