"""Validated data contracts for Samsung company metadata."""
from pydantic import BaseModel

class CompanySource(BaseModel):
    source_id: str
    source_type: str
    url: str
    authority: str
    live_connection: bool = False

class CompanyProfile(BaseModel):
    company_id: str
    canonical_name: str
    record_type: str = "company"
    profile_status: str
    data_status: str
    sources: list[CompanySource]
    limitations: list[str]
