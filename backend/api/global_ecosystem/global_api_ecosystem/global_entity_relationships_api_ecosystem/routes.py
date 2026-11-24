"""Shared relationship directory routes."""
from fastapi import APIRouter, HTTPException, Query
from .service import load_relationships, search_relationships

router = APIRouter(tags=["GLOBAL ENTITY RELATIONSHIPS API"])


@router.get("/global/entity-relationships/status")
def relationship_status():
    records = load_relationships()
    return {"success": True, "status": "ready_with_records" if records else "registry_empty", "count": len(records), "registry_mode": "local_json_read_only"}


@router.get("/global/entity-relationships")
def relationship_search(entity_id: str | None = Query(default=None), relationship_type: str | None = Query(default=None)):
    try:
        records = search_relationships(entity_id, relationship_type)
    except ValueError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    return {"success": True, "count": len(records), "items": records}
