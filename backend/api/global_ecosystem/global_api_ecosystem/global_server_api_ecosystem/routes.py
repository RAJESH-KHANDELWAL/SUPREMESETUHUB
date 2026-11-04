"""Routes for the Global Server API Ecosystem."""

from fastapi import APIRouter

from .service import get_server_ecosystem_status

router = APIRouter(prefix="/global/server", tags=["Global Server API Ecosystem"])


@router.get("/status")
def server_ecosystem_status() -> dict[str, str]:
    """Return the basic status of this ecosystem module."""
    return get_server_ecosystem_status()
