"""Typed data models for District Administration Jobs."""
from pydantic import BaseModel, Field

class JobWorkRecord(BaseModel):
    id: str
    title: str
    employer_name: str | None = None
    jurisdiction: str | None = None
    work_location: str | None = None
    engagement_type: str | None = None
    source_url: str | None = None
    source_published_at: str | None = None
    last_verified_at: str | None = None
    domain_details: dict[str, str] = Field(default_factory=dict)
    taxonomy_status: str = "taxonomy_only"

class JobFamilySummary(BaseModel):
    category_id: str = "local_jobs"
    job_family_id: str = "district_administration_jobs"
    name: str = "District Administration Jobs"
    role_examples: list[str] = Field(default_factory=list)
    required_domain_fields: list[str] = Field(default_factory=list)
