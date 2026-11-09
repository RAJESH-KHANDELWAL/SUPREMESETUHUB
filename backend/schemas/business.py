"""Validated request schemas for business and enterprise resources."""
from typing import Any
from pydantic import BaseModel, Field

class BusinessCreateRequest(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    category: str = Field(default="", max_length=100)
    location: str = Field(default="", max_length=300)
    website: str = Field(default="", max_length=2048)
    public_contact: str = Field(default="", max_length=300)
    source: str = Field(default="", max_length=100)
    metadata: dict[str, Any] = Field(default_factory=dict)
    # Optional fields preserve compatibility with existing clients.
    legal_name: str = Field(default="", max_length=250)
    business_type: str = Field(default="SMALL_BUSINESS", max_length=50)
    industry: str = Field(default="", max_length=120)
    employee_count: int | None = Field(default=None, ge=0, le=100_000_000)
    headquarters: str = Field(default="", max_length=300)
    parent_company_id: str = Field(default="", max_length=100)
    annual_revenue_band: str = Field(default="", max_length=80)
    operating_regions: list[str] = Field(default_factory=list, max_length=100)
    departments: list[str] = Field(default_factory=list, max_length=200)
    tags: list[str] = Field(default_factory=list, max_length=100)
    compliance_status: str = Field(default="UNSPECIFIED", max_length=50)

class BusinessStatusRequest(BaseModel):
    status: str = Field(min_length=1, max_length=32)
