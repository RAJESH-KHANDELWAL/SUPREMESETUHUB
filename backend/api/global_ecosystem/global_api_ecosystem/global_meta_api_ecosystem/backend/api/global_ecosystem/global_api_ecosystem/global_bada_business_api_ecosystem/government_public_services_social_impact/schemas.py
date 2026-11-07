"""Response schemas for Government, Public Services & Social Impact."""
from pydantic import BaseModel

class PublicImpactCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]

class PublicImpactListResponse(BaseModel):
    success: bool
    count: int
    categories: list[PublicImpactCategory]

class PublicImpactDetailResponse(BaseModel):
    success: bool
    category: PublicImpactCategory
