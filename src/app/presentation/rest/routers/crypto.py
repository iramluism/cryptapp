from fastapi import APIRouter
from fastapi_injector import Injected

from app.application.services import CollectAndProcessCryptoDataService
from app.application.services import GetCryptoBidsService
from app.presentation.rest import serializers

router = APIRouter()


@router.post("/collect")
async def collect_data(
    service: CollectAndProcessCryptoDataService = Injected(
        CollectAndProcessCryptoDataService
    ),
):
    return await service.execute()


@router.get("/{symbol}/bids")
async def get_bids(
    symbol: str,
    service: GetCryptoBidsService = Injected(GetCryptoBidsService),
    serializer: serializers.BidsEntriesSerializer = Injected(
        serializers.BidsEntriesSerializer
    ),
):
    bids = await service.execute(symbol)
    return await serializer.to_dict(bids)
