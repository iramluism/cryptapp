from fastapi import APIRouter

router = APIRouter(prefix="/tools")


@router.get("/health")
async def health_check():
    return {"status": "ok"}
