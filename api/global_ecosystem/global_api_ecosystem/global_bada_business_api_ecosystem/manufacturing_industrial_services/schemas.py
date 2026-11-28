"""Pydantic response schemas for manufacturing and factory services."""
from pydantic import BaseModel

class ManufacturingCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]

class ManufacturingCategoryListResponse(BaseModel):
    success: bool
    count: int
    categories: list[ManufacturingCategory]

class ManufacturingCategoryDetailResponse(BaseModel):
    success: bool
    category: ManufacturingCategory

class ManufacturingBusinessDomain(BaseModel):
    id: str
    name: str
    category_id: str
    description: str

class ManufacturingBusinessDomainListResponse(BaseModel):
    success: bool
    count: int
    business_domains: list[ManufacturingBusinessDomain]

class ManufacturingBusinessDomainDetailResponse(BaseModel):
    success: bool
    business_domain: ManufacturingBusinessDomain
