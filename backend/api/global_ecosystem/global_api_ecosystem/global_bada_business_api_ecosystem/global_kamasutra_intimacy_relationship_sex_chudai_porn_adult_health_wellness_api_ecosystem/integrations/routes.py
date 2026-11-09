"""Read-only discovery endpoints for relationship and intimacy integrations."""
from fastapi import APIRouter, Query
from .schemas import IntegrationEntry
from .service import list_entries

router = APIRouter(prefix="/integrations", tags=["GLOBAL INTIMACY INTEGRATIONS"])

@router.get("/catalog", response_model=list[IntegrationEntry])
def integration_catalog(category_id: str | None = Query(default=None, max_length=64)):
    """List planned integration boundaries; records are not live connectors."""
    return list_entries(category_id)
