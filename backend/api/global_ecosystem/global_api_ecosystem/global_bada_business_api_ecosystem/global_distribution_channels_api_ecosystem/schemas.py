from pydantic import BaseModel, Field

class DistributionChannelBusinessProfile(BaseModel):
    business_types: list[str] = Field(default_factory=list)
    customer_types: list[str] = Field(default_factory=list)
    operating_modes: list[str] = Field(default_factory=list)
    revenue_models: list[str] = Field(default_factory=list)
    inbound_from: list[str] = Field(default_factory=list)
    handoff_to: list[str] = Field(default_factory=list)
    core_activities: list[str] = Field(default_factory=list)
    typical_records: list[str] = Field(default_factory=list)
    onboarding_data: list[str] = Field(default_factory=list)

class DistributionChannel(BaseModel):
    id: str
    name: str
    stage: str
    participants: list[str]
    next_channels: list[str]
    business_profile: DistributionChannelBusinessProfile | None = None

class DistributionChannelListResponse(BaseModel):
    success: bool
    count: int
    channels: list[DistributionChannel]

class DistributionChannelDetailResponse(BaseModel):
    success: bool
    channel: DistributionChannel
