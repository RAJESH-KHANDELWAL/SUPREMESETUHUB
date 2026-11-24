"""Pydantic profile model for company directory records."""
from typing import List, Optional
from pydantic import BaseModel, Field
class CompanyDirectoryProfile(BaseModel):
    company_id: str
    name: str
    entity_type: str
    record_type: str = "company"
    country_code: Optional[str] = None
    legal_status: Optional[str] = None
    verification_status: str = "unverified"
    industries: List[str] = Field(default_factory=list)
    website: Optional[str] = None
    description: Optional[str] = None
    source_urls: List[str] = Field(default_factory=list)
class CompanyDirectoryCatalog(BaseModel):
    record_type: str = "company"
    name: str = "Companies"
    entity_types: List[str]
    registry_status: str = "taxonomy_only"
