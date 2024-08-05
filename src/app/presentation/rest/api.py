from fastapi import FastAPI

from app.domain.exceptions import DomainException
from app.infrastructure.setup import setup_fastapi_app
from app.presentation.rest.handlers import handle_domain_exception
from app.presentation.rest.routers import crypto_router
from app.presentation.rest.routers import tools_router


def setup_app_routers(app: FastAPI) -> None:
    app.include_router(tools_router, tags=["tools"])
    app.include_router(crypto_router, tags=["crypto"])


def create_app():
    app = FastAPI()

    app.add_exception_handler(DomainException, handle_domain_exception)

    setup_fastapi_app(app)
    setup_app_routers(app)

    return app
