from fastapi import FastAPI
from presentation.rest.routers import tools_router


def setup_app_routers(app: FastAPI) -> None:
    app.include_router(tools_router, prefix="/tools", tags=["tools"])


def create_app():
    app = FastAPI()

    setup_app_routers(app)

    return app
