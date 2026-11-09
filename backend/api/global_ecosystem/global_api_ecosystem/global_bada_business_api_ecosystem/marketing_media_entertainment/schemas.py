from pydantic import BaseModel, Field


class MarketingCategory(BaseModel):
    id: str
    name: str
    channels: list[str] = Field(default_factory=list)
    subcategories: list[str]


class MarketingListResponse(BaseModel):
    success: bool
    count: int
    categories: list[MarketingCategory]


class MarketingDetailResponse(BaseModel):
    success: bool
    category: MarketingCategory
