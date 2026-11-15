"""Business domain record."""
from __future__ import annotations
from dataclasses import asdict, dataclass
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
    metadata: dict[str, Any] | None = None
    legal_name: str = ""
    business_type: str = "SMALL_BUSINESS"
    industry: str = ""
    employee_count: int | None = None
    headquarters: str = ""
    parent_company_id: str = ""
    annual_revenue_band: str = ""
    operating_regions: list[str] | None = None
    departments: list[str] | None = None
    tags: list[str] | None = None
    compliance_status: str = "UNSPECIFIED"
    created_at: str | None = None
    updated_at: str | None = None

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        value["metadata"] = self.metadata or {}
        value["operating_regions"] = self.operating_regions or []
        value["departments"] = self.departments or []
        value["tags"] = self.tags or []
        return value
