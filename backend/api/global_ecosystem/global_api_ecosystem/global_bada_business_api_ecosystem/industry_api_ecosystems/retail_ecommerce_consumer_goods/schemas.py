"""Response schemas."""
from pydantic import BaseModel
class RetailCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]
class RetailListResponse(BaseModel):
    success: bool
    count: int
    categories: list[RetailCategory]
class RetailDetailResponse(BaseModel):
    success: bool
    category: RetailCategory
