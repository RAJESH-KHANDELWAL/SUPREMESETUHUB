"""API schemas for Overseas Skilled Employment."""
from pydantic import BaseModel, Field

class JobWorkCreateRequest(BaseModel):
    title: str
    employer_name: str | None = None
    jurisdiction: str | None = None
    work_location: str | None = None
    engagement_type: str | None = None
    source_url: str | None = None
    domain_details: dict[str, str] = Field(default_factory=dict)

class JobFamilyResponse(BaseModel):
    category_id: str
    job_family_id: str
    name: str
    role_examples: list[str]
    required_domain_fields: list[str]
    taxonomy_status: str = "taxonomy_only"
