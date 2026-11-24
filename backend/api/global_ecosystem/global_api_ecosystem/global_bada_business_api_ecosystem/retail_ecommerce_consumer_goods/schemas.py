"""Retail and consumer-goods response schemas."""
from pydantic import BaseModel


class RetailCategory(BaseModel):
    id: str
    name: str
    subcategories: list[str]


class RetailBusinessDomain(BaseModel):
    id: str
    name: str
    category_id: str


class RetailListResponse(BaseModel):
    success: bool
    count: int
    categories: list[RetailCategory]


class RetailDetailResponse(BaseModel):
    success: bool
    category: RetailCategory


class RetailBusinessDomainListResponse(BaseModel):
    success: bool
    count: int
    domains: list[RetailBusinessDomain]


class RetailBusinessDomainDetailResponse(BaseModel):
    success: bool
    domain: RetailBusinessDomain
