from pydantic import BaseModel

class DistributionChannel(BaseModel):
    id: str
    name: str
    stage: str
    participants: list[str]
    next_channels: list[str]

class DistributionChannelListResponse(BaseModel):
    success: bool
    count: int
    channels: list[DistributionChannel]

class DistributionChannelDetailResponse(BaseModel):
    success: bool
    channel: DistributionChannel
