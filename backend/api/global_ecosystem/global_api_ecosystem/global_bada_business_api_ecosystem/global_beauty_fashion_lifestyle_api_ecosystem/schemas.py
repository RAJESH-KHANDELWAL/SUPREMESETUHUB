from pydantic import BaseModel


class BeautyCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]


class BeautyBusinessDomain(BaseModel):
    id: str
    name: str
    category_id: str


class BeautyCategoryListResponse(BaseModel):
    success: bool
    count: int
    categories: list[BeautyCategory]


class BeautyCategoryDetailResponse(BaseModel):
    success: bool
    category: BeautyCategory


class BeautyBusinessDomainListResponse(BaseModel):
    success: bool
    count: int
    domains: list[BeautyBusinessDomain]


class BeautyBusinessDomainDetailResponse(BaseModel):
    success: bool
    domain: BeautyBusinessDomain
