import asyncio
import importlib
from typing import Optional

from celery import Celery
from fastapi import FastAPI
from fastapi_injector import attach_injector
from injector import Injector
from injector import singleton
from simple_settings import settings


def _get_object(obj_path):
    module_path, class_name = obj_path.rsplit(".", 1)
    module = importlib.import_module(module_path)
    obj = getattr(module, class_name)
    return obj


def get_data_source():
    data_source_name = settings.REPOSITORY_DATA_SOURCE.get("name")
    data_source_cls = _get_object(data_source_name)

    sources = settings.REPOSITORY_DATA_SOURCE.get("sources", {})

    kwargs = {key: _get_object(value)() for key, value in sources.items()}

    data_source = data_source_cls(**kwargs)
    return data_source


def setup_task(task_definition):
    injector = setup_dependencies()

    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()

        async def task():
            return await injector.call_with_injection(task_definition, *args, **kwargs)

        return loop.run_until_complete(task())

    return wrapper


def setup_dependencies(injector: Optional[Injector] = None) -> Injector:
    if not injector:
        injector = Injector()

    data_source = get_data_source()

    for interface, implementation in settings.DEPENDENCIES.items():
        injector.binder.bind(
            interface, to=implementation(data_source=data_source), scope=singleton
        )

    return injector


def setup_fastapi_app(app: FastAPI) -> None:
    injector = setup_dependencies()
    attach_injector(app, injector)


def setup_celery_app(app: Celery) -> None:
    setup_dependencies()
