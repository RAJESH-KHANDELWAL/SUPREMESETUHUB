from pydantic import BaseModel, Field


class InternationalTradeCategory(BaseModel):
    id: str
    name: str
    channels: list[str] = Field(default_factory=list)
    subcategories: list[str]


class InternationalTradeListResponse(BaseModel):
    success: bool
    count: int
    categories: list[InternationalTradeCategory]


class InternationalTradeDetailResponse(BaseModel):
    success: bool
    category: InternationalTradeCategory
