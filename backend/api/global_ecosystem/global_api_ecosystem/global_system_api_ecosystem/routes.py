"""FastAPI routes for GLOBAL SYSTEM API ECOSYSTEM."""

from fastapi import APIRouter
from .service import get_ecosystem_status

router = APIRouter(prefix="/global/system", tags=["GLOBAL SYSTEM API ECOSYSTEM"])


@router.get("/status")
def ecosystem_status() -> dict[str, str]:
    """Return this module's basic status."""
    return get_ecosystem_status()
