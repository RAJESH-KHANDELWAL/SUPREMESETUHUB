"""FastAPI routes for GLOBAL WEBSITE API ECOSYSTEM."""

from fastapi import APIRouter
from .service import get_ecosystem_status

router = APIRouter(prefix="/global/website", tags=["GLOBAL WEBSITE API ECOSYSTEM"])


@router.get("/status")
def ecosystem_status() -> dict[str, str]:
    return get_ecosystem_status()
