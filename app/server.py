from fastapi import FastAPI
import uvicorn
from apis.groups import create_group
from apis.users import create_user, update_user
from apis.notifications import create_notification
from apis.fcm import messaging_js, notification

app = FastAPI()
app.include_router(create_group.router)
app.include_router(create_user.router)
app.include_router(update_user.router)
app.include_router(create_notification.router)
app.include_router(notification.router)
app.include_router(messaging_js.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
