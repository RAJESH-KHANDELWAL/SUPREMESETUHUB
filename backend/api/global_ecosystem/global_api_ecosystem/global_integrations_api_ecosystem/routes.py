"""FastAPI routes for GLOBAL INTEGRATIONS API ECOSYSTEM."""

from fastapi import APIRouter
from .service import get_ecosystem_status

router = APIRouter(prefix="/global/integrations", tags=["GLOBAL INTEGRATIONS API ECOSYSTEM"])


@router.get("/status")
def ecosystem_status() -> dict[str, str]:
    return get_ecosystem_status()
