"""Routes for the global VPS API ecosystem."""

from fastapi import APIRouter

router = APIRouter(prefix="/global/vps", tags=["global-vps"])

@router.get("/status")
def vps_ecosystem_status() -> dict[str, object]:
    """Report catalog readiness without claiming provider connectivity."""
    return {
        "ecosystem_id": "VPS",
        "status": "catalog_scaffold",
        "provider_count": 20,
        "live_connections_verified": False,
        "note": "Provider folders are catalog scaffolds until individually implemented and tested.",
    }
