"""API routes for server service-type catalog."""
from fastapi import APIRouter
from .service import list_entries

router = APIRouter(prefix="/services", tags=["GLOBAL SERVER SERVICES"])

@router.get("")
def server_services():
    items = list_entries()
    return {"success": True, "count": len(items), "services": items}
