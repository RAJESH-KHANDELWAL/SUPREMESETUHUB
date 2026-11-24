"""Pydantic response models for the global Company / Companies API."""
from typing import List, Optional
from pydantic import BaseModel, Field

class CompanyRecord(BaseModel):
    """Normalized profile; record_type is canonical Company, Enterprise or Corporate Group; legacy Freelancer records are compatibility-only."""
    company_id: str
    name: str
    entity_type: str
    record_type: str = "company"
    country_code: Optional[str] = None
    legal_status: Optional[str] = None
    verification_status: str = "unverified"
    industries: List[str] = Field(default_factory=list)
    company_types: List[str] = Field(default_factory=list)
    website: Optional[str] = None
    description: Optional[str] = None
    headquarters: Optional[str] = None
    aliases: List[str] = Field(default_factory=list)
    source_urls: List[str] = Field(default_factory=list)
    last_verified_at: Optional[str] = None

class CompanyListResponse(BaseModel):
    total: int
    limit: int
    offset: int
    items: List[CompanyRecord]

class CompanyAlphabetResponse(BaseModel):
    total: int
    letters: dict[str, int]

class CompanyApiStatus(BaseModel):
    ecosystem: str
    status: str
    company_api: str
    companies_api: str
    registry_records: int
    source_count: int
    source_countries: List[str]
    registry_mode: str
    source_mode: str
    note: str
