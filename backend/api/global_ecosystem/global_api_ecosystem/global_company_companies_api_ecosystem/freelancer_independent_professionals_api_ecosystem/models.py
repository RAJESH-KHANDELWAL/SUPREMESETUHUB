"""Pydantic profile model for freelancer directory records."""
from typing import List, Optional
from pydantic import BaseModel, Field
class FreelancerDirectoryProfile(BaseModel):
    company_id: str
    name: str
    entity_type: str
    record_type: str = "freelancer"
    country_code: Optional[str] = None
    legal_status: Optional[str] = None
    verification_status: str = "unverified"
    industries: List[str] = Field(default_factory=list)
    website: Optional[str] = None
    description: Optional[str] = None
    source_urls: List[str] = Field(default_factory=list)
class FreelancerDirectoryCatalog(BaseModel):
    record_type: str = "freelancer"
    name: str = "Freelancers"
    entity_types: List[str]
    registry_status: str = "taxonomy_only"
