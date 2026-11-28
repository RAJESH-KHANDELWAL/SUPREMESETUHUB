"""Private readiness endpoint for CORE, database, and storage."""
from fastapi import APIRouter

from backend.core.readiness import CoreReadinessService

router = APIRouter(tags=["CORE Readiness"])


@router.get("/api/v1/core/readiness")
def core_readiness():
    """Return component readiness; authentication is enforced by app middleware."""
    return CoreReadinessService().snapshot()
