from fastapi import APIRouter, HTTPException, Query

from .schemas import DistributionChannelDetailResponse, DistributionChannelListResponse
from .service import DistributionChannelsService

router = APIRouter(
    prefix="/distribution-channels",
    tags=["GLOBAL BADA BUSINESS - DISTRIBUTION CHANNELS"],
)
service = DistributionChannelsService()

@router.get("/status")
def status():
    return service.get_status()

@router.get("/channels", response_model=DistributionChannelListResponse)
def channels(q: str | None = Query(default=None, min_length=1, max_length=100)):
    items = service.list_channels(q)
    return {"success": True, "count": len(items), "channels": items}

@router.get("/channels/{channel_id}", response_model=DistributionChannelDetailResponse)
def channel(channel_id: str):
    item = service.get_channel(channel_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "CHANNEL_NOT_FOUND", "channel_id": channel_id})
    return {"success": True, "channel": item}
