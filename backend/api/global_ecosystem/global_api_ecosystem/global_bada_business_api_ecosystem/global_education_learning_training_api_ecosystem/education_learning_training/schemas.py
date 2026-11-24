"""Pydantic response schemas for the education domain API."""
from pydantic import BaseModel

class EducationCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]

class EducationCategoryListResponse(BaseModel):
    success: bool
    count: int
    categories: list[EducationCategory]

class EducationCategoryDetailResponse(BaseModel):
    success: bool
    category: EducationCategory
