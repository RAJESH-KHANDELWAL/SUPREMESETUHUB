from fastapi import APIRouter, HTTPException, Query

from .schemas import ArtsCultureDetailResponse, ArtsCultureListResponse
from .service import ArtsCultureHeritageService

router = APIRouter(
    prefix="/arts-culture-heritage",
    tags=["GLOBAL BADA BUSINESS - ARTS, CULTURE & HERITAGE"],
)
service = ArtsCultureHeritageService()


@router.get("/status")
def status():
    return service.get_status()


@router.get("/categories", response_model=ArtsCultureListResponse)
def categories(
    q: str | None = Query(default=None, min_length=1, max_length=100),
    channel: str | None = Query(default=None, pattern="^(online|offline|hybrid)$"),
):
    items = service.list_categories(query=q, channel=channel)
    return {"success": True, "count": len(items), "categories": items}


@router.get("/categories/{category_id}", response_model=ArtsCultureDetailResponse)
def category(category_id: str):
    item = service.get_category(category_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "CATEGORY_NOT_FOUND", "category_id": category_id})
    return {"success": True, "category": item}
