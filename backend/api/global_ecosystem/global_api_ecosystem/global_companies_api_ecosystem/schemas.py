"""Pydantic response models for the global Company / Companies API."""

from typing import List, Optional

from pydantic import BaseModel, Field


class CompanyRecord(BaseModel):
    """Normalized company or business profile; verification is explicit."""

    company_id: str
    name: str
    entity_type: str
    country_code: Optional[str] = None
    legal_status: Optional[str] = None
    verification_status: str = "unverified"
    industries: List[str] = Field(default_factory=list)
    company_types: List[str] = Field(default_factory=list)
    website: Optional[str] = None
    description: Optional[str] = None
    headquarters: Optional[str] = None
    aliases: List[str] = Field(default_factory=list)


class CompanyListResponse(BaseModel):
    total: int
    limit: int
    offset: int
    items: List[CompanyRecord]


class CompanyApiStatus(BaseModel):
    ecosystem: str
    status: str
    company_api: str
    companies_api: str
    registry_records: int
    registry_mode: str
    note: str
