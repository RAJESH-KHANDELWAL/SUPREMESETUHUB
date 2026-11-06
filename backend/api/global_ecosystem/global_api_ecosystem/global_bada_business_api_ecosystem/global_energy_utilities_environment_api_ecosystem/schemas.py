"""Response schemas for Energy, Utilities & Environment."""
from pydantic import BaseModel

class EnergyEnvironmentCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]

class EnergyEnvironmentListResponse(BaseModel):
    success: bool
    count: int
    categories: list[EnergyEnvironmentCategory]

class EnergyEnvironmentDetailResponse(BaseModel):
    success: bool
    category: EnergyEnvironmentCategory

class EnergyBusinessDomain(BaseModel):
    id: str
    name: str
    category_id: str
    description: str

class EnergyBusinessDomainListResponse(BaseModel):
    success: bool
    count: int
    business_domains: list[EnergyBusinessDomain]

class EnergyBusinessDomainDetailResponse(BaseModel):
    success: bool
    business_domain: EnergyBusinessDomain
