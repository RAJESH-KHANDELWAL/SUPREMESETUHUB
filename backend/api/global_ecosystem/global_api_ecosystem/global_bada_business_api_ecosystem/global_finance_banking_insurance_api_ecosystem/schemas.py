"""Pydantic response schemas for Finance, Banking & Insurance."""
from pydantic import BaseModel

class FinanceCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]

class FinanceCategoryListResponse(BaseModel):
    success: bool
    count: int
    categories: list[FinanceCategory]

class FinanceCategoryDetailResponse(BaseModel):
    success: bool
    category: FinanceCategory
