"""Pydantic response schemas for the agriculture domain API."""
from pydantic import BaseModel

class AgricultureCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]

class AgricultureCategoryListResponse(BaseModel):
    success: bool
    count: int
    categories: list[AgricultureCategory]

class AgricultureCategoryDetailResponse(BaseModel):
    success: bool
    category: AgricultureCategory
