from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="resources")

router = APIRouter()


@router.get("/get-fcm-token", response_class=HTMLResponse, include_in_schema=False)
async def get_token_and_notification(request: Request):
    return templates.TemplateResponse("notification.html", {"request": request})
