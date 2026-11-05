"""Pydantic response schemas for Jobs, Careers & Employment."""
from pydantic import BaseModel

class JobsCareersCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]

class JobsCareersCategoryListResponse(BaseModel):
    success: bool
    count: int
    categories: list[JobsCareersCategory]

class JobsCareersCategoryDetailResponse(BaseModel):
    success: bool
    category: JobsCareersCategory
