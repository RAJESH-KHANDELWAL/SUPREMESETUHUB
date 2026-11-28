"""Pydantic response schemas for Healthcare & Life Sciences."""
from pydantic import BaseModel

class HealthcareCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]

class HealthcareCategoryListResponse(BaseModel):
    success: bool
    count: int
    categories: list[HealthcareCategory]

class HealthcareCategoryDetailResponse(BaseModel):
    success: bool
    category: HealthcareCategory
