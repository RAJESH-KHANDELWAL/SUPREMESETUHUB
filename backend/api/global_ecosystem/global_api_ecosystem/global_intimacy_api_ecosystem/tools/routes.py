"""Read-only catalog routes for relationship and intimacy tools."""
from fastapi import APIRouter
from .schemas import ToolEntry
from .service import list_entries

router = APIRouter(prefix="/tools", tags=["GLOBAL INTIMACY TOOLS"])

@router.get("/catalog", response_model=list[ToolEntry])
def tool_catalog():
    """List tool definitions; these entries do not perform live checks."""
    return list_entries()
