from pydantic import BaseModel


class AviationAerospaceCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]


class AviationBusinessDomain(BaseModel):
    id: str
    name: str
    category_id: str


class AviationAerospaceListResponse(BaseModel):
    success: bool
    count: int
    categories: list[AviationAerospaceCategory]


class AviationAerospaceDetailResponse(BaseModel):
    success: bool
    category: AviationAerospaceCategory


class AviationBusinessDomainListResponse(BaseModel):
    success: bool
    count: int
    domains: list[AviationBusinessDomain]


class AviationBusinessDomainDetailResponse(BaseModel):
    success: bool
    domain: AviationBusinessDomain
