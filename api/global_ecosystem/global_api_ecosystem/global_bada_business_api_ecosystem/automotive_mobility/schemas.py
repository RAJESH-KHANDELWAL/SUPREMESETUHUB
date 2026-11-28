from pydantic import BaseModel


class AutomotiveMobilityCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]


class AutomotiveBusinessDomain(BaseModel):
    id: str
    name: str
    category_id: str


class AutomotiveMobilityListResponse(BaseModel):
    success: bool
    count: int
    categories: list[AutomotiveMobilityCategory]


class AutomotiveMobilityDetailResponse(BaseModel):
    success: bool
    category: AutomotiveMobilityCategory


class AutomotiveBusinessDomainListResponse(BaseModel):
    success: bool
    count: int
    domains: list[AutomotiveBusinessDomain]


class AutomotiveBusinessDomainDetailResponse(BaseModel):
    success: bool
    domain: AutomotiveBusinessDomain
