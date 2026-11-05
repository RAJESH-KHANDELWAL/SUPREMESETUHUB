"""Typed data models for Government Agriculture Posts."""
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
    category_id: str = "government_jobs"
    job_family_id: str = "government_agriculture_posts"
    name: str = "Government Agriculture Posts"
    role_examples: list[str] = Field(default_factory=list)
    required_domain_fields: list[str] = Field(default_factory=list)
