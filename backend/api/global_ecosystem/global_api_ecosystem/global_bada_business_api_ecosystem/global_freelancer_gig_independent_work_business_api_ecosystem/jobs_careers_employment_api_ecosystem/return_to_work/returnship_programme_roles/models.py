"""Typed data models for Returnship Programme Roles."""
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
    category_id: str = "return_to_work"
    job_family_id: str = "returnship_programme_roles"
    name: str = "Returnship Programme Roles"
    role_examples: list[str] = Field(default_factory=list)
    required_domain_fields: list[str] = Field(default_factory=list)
