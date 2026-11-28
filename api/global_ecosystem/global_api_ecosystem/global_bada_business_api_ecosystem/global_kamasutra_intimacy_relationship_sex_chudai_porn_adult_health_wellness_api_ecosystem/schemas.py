"""Pydantic response schemas for the adult wellness taxonomy."""
from pydantic import BaseModel

class AdultWellnessCategory(BaseModel):
    id: str
    name: str
    folder: str
    subdomains: list[str]
    coverage: list[str]
    channels: list[str]
    age_restriction: str
    status: str

class AdultWellnessListResponse(BaseModel):
    success: bool
    count: int
    categories: list[AdultWellnessCategory]

class AdultWellnessDetailResponse(BaseModel):
    success: bool
    category: AdultWellnessCategory
