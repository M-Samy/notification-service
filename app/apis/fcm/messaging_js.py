from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="resources")

router = APIRouter()


@router.get("/firebase-messaging-sw.js", include_in_schema=False)
async def get_fcm_messages(request: Request):
    return templates.TemplateResponse("firebase-messaging-sw.js", {"request": request}, media_type="text/javascript")
