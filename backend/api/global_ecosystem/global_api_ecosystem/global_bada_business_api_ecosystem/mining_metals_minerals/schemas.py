"""Response schemas for Mining, Metals & Minerals."""
from pydantic import BaseModel

class MiningMetalsCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]

class MiningMetalsListResponse(BaseModel):
    success: bool
    count: int
    categories: list[MiningMetalsCategory]

class MiningMetalsDetailResponse(BaseModel):
    success: bool
    category: MiningMetalsCategory

class MiningBusinessDomain(BaseModel):
    id: str
    name: str
    category_id: str
    description: str

class MiningBusinessDomainListResponse(BaseModel):
    success: bool
    count: int
    business_domains: list[MiningBusinessDomain]

class MiningBusinessDomainDetailResponse(BaseModel):
    business_domain: MiningBusinessDomain
