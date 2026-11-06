from pydantic import BaseModel, Field


class ArtsCultureCategory(BaseModel):
    id: str
    name: str
    channels: list[str] = Field(default_factory=list)
    subcategories: list[str]


class ArtsCultureListResponse(BaseModel):
    success: bool
    count: int
    categories: list[ArtsCultureCategory]


class ArtsCultureDetailResponse(BaseModel):
    success: bool
    category: ArtsCultureCategory
