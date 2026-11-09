"""FastAPI routes for GLOBAL SERVICES API ECOSYSTEM."""

from fastapi import APIRouter
from .service import get_ecosystem_status

router = APIRouter(prefix="/global/services", tags=["GLOBAL SERVICES API ECOSYSTEM"])


@router.get("/status")
def ecosystem_status() -> dict[str, str]:
    return get_ecosystem_status()
