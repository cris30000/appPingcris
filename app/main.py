from fastapi import FastAPI
from app.routes.ping_routes import router as ping_router
from app.routes.user_routes import router as user_router

app = FastAPI(title="AppPoint API")

app.include_router(ping_router)
app.include_router(user_router)