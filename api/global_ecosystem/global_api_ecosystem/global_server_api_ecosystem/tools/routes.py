"""API routes for SERVER ecosystem tool metadata."""
from fastapi import APIRouter
from .service import list_entries

router = APIRouter(prefix="/tools", tags=["GLOBAL SERVER TOOLS"])

@router.get("")
def server_tools():
    items = list_entries()
    return {"success": True, "count": len(items), "tools": items}
