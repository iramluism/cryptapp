from fastapi import APIRouter
from fastapi_injector import Injected

from app.application.services import CollectAndProcessCryptoDataService

router = APIRouter()


@router.post("/collect")
async def collect_data(
    service: CollectAndProcessCryptoDataService = Injected(
        CollectAndProcessCryptoDataService
    ),
):
    return await service.execute()
