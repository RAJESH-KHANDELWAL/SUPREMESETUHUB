"""Business and enterprise domain model."""
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Business:
    business_id: str
    owner_id: str
    name: str
    category: str = ""
    location: str = ""
    website: str = ""
    public_contact: str = ""
    source: str = ""
    status: str = "ACTIVE"
    verified: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)
    legal_name: str = ""
    business_type: str = "SMALL_BUSINESS"
    industry: str = ""
    employee_count: int | None = None
    headquarters: str = ""
    parent_company_id: str = ""
    annual_revenue_band: str = ""
    operating_regions: list[str] = field(default_factory=list)
    departments: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    compliance_status: str = "UNSPECIFIED"

    def to_dict(self) -> dict[str, Any]:
        return {
            "business_id": self.business_id, "owner_id": self.owner_id,
            "name": self.name, "category": self.category, "location": self.location,
            "website": self.website, "public_contact": self.public_contact,
            "source": self.source, "status": self.status, "verified": self.verified,
            "metadata": self.metadata, "legal_name": self.legal_name,
            "business_type": self.business_type, "industry": self.industry,
            "employee_count": self.employee_count, "headquarters": self.headquarters,
            "parent_company_id": self.parent_company_id,
            "annual_revenue_band": self.annual_revenue_band,
            "operating_regions": list(self.operating_regions),
            "departments": list(self.departments), "tags": list(self.tags),
            "compliance_status": self.compliance_status,
        }
