"""Response schemas."""
from pydantic import BaseModel
class RealEstateCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]
class RealEstateListResponse(BaseModel):
    success: bool
    count: int
    categories: list[RealEstateCategory]
class RealEstateDetailResponse(BaseModel):
    success: bool
    category: RealEstateCategory
