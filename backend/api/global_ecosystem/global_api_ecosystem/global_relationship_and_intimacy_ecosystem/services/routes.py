"""Read-only catalog routes for relationship and intimacy services."""
from fastapi import APIRouter, Query
from .schemas import ServiceEntry
from .service import list_entries

router = APIRouter(prefix="/services", tags=["GLOBAL INTIMACY SERVICES"])

@router.get("/catalog", response_model=list[ServiceEntry])
def service_catalog(category_id: str | None = Query(default=None, max_length=64)):
    """List service categories; availability and provider details require validation."""
    return list_entries(category_id)
