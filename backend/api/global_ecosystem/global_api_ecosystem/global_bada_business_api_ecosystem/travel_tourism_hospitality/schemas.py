from pydantic import BaseModel
class TravelCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]
class TravelListResponse(BaseModel):
    success: bool
    count: int
    categories: list[TravelCategory]
class TravelDetailResponse(BaseModel):
    success: bool
    category: TravelCategory
