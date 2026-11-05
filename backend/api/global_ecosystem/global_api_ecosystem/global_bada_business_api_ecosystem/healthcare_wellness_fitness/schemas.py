"""Pydantic response schemas for Healthcare, Wellness & Fitness."""
from pydantic import BaseModel

class WellnessCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]

class WellnessCategoryListResponse(BaseModel):
    success: bool
    count: int
    categories: list[WellnessCategory]

class WellnessCategoryDetailResponse(BaseModel):
    success: bool
    category: WellnessCategory
