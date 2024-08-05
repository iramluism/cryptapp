from fastapi import APIRouter
from fastapi_injector import Injected

from app.application.services import CollectAndProcessCryptoDataService
from app.application.services import GetCryptoAsksService
from app.application.services import GetCryptoBidsService
from app.application.services import GetCryptoService
from app.presentation.rest import serializers

router = APIRouter(
    prefix="/cryptos",
)


@router.post("/collect")
async def collect_data(
    service: CollectAndProcessCryptoDataService = Injected(
        CollectAndProcessCryptoDataService
    ),
):
    return await service.execute()


@router.get("/{symbol}")
async def get_crypto(
    symbol: str,
    service: GetCryptoService = Injected(GetCryptoService),
    serializer: serializers.GenericCryptoDataSerializer = Injected(
        serializers.GenericCryptoDataSerializer
    ),
):
    bids = await service.execute(symbol)
    return await serializer.to_dict(bids)


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


@router.get("/{symbol}/asks")
async def get_asks(
    symbol: str,
    service: GetCryptoAsksService = Injected(GetCryptoAsksService),
    serializer: serializers.AsksEntriesSerializer = Injected(
        serializers.AsksEntriesSerializer
    ),
):
    asks = await service.execute(symbol)
    return await serializer.to_dict(asks)
