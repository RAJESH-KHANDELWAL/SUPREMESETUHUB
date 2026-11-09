"""API routes for SERVER cross-layer integration metadata."""
from fastapi import APIRouter
from .service import list_entries

router = APIRouter(prefix="/integrations", tags=["GLOBAL SERVER INTEGRATIONS"])

@router.get("")
def server_integrations():
    items = list_entries()
    return {"success": True, "count": len(items), "integrations": items}
