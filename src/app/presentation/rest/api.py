from fastapi import FastAPI

from app.infrastructure.setup import setup_fastapi_app
from app.presentation.rest.routers import tools_router


def setup_app_routers(app: FastAPI) -> None:
    app.include_router(tools_router, prefix="/tools", tags=["tools"])


def create_app():
    app = FastAPI()

    setup_fastapi_app(app)
    setup_app_routers(app)

    return app
