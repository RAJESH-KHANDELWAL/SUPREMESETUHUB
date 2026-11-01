"""Validated response models for the OpenAI company profile adapter."""
from pydantic import BaseModel, HttpUrl

class CompanySource(BaseModel):
    source_id: str
    source_type: str
    url: HttpUrl
    authority: str
    live_connection: bool = False

class CompanyProfileResponse(BaseModel):
    success: bool = True
    company_id: str
    canonical_name: str
    record_type: str = "company"
    profile_status: str
    data_status: str
    description: str | None = None
    sources: list[CompanySource]
    limitations: list[str]
