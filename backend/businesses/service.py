"""Business domain service for business and enterprise profiles."""
from typing import Any
from backend.businesses.model import Business

class BusinessService:
    """Coordinates business-domain operations."""
    ALLOWED_TYPES = {"SOLE_PROPRIETORSHIP", "SMALL_BUSINESS", "MEDIUM_BUSINESS", "LARGE_BUSINESS", "ENTERPRISE", "NONPROFIT", "PUBLIC_SECTOR"}

    def __init__(self):
        self.businesses: dict[str, Business] = {}

    def create_business(self, business_id: str, owner_id: str, name: str,
        category: str = "", location: str = "", website: str = "",
        public_contact: str = "", source: str = "", status: str = "ACTIVE",
        verified: bool = False, metadata: dict[str, Any] | None = None,
        legal_name: str = "", business_type: str = "SMALL_BUSINESS",
        industry: str = "", employee_count: int | None = None,
        headquarters: str = "", parent_company_id: str = "",
        annual_revenue_band: str = "", operating_regions: list[str] | None = None,
        departments: list[str] | None = None, tags: list[str] | None = None,
        compliance_status: str = "UNSPECIFIED") -> Business:
        if business_id in self.businesses:
            raise ValueError(f"Business already exists: {business_id}")
        normalized_type = business_type.strip().upper() or "SMALL_BUSINESS"
        if normalized_type not in self.ALLOWED_TYPES:
            raise ValueError("Unsupported business_type")
        if employee_count is not None and employee_count < 0:
            raise ValueError("employee_count cannot be negative")
        record = Business(
            business_id=business_id, owner_id=owner_id, name=name,
            category=category, location=location, website=website,
            public_contact=public_contact, source=source, status=status,
            verified=verified, metadata=metadata or {}, legal_name=legal_name,
            business_type=normalized_type, industry=industry,
            employee_count=employee_count, headquarters=headquarters,
            parent_company_id=parent_company_id, annual_revenue_band=annual_revenue_band,
            operating_regions=list(operating_regions or []), departments=list(departments or []),
            tags=list(tags or []), compliance_status=compliance_status.strip().upper() or "UNSPECIFIED")
        self.businesses[business_id] = record
        return record

    def get_business(self, business_id: str) -> Business | None:
        return self.businesses.get(business_id)
    def list_businesses(self) -> list[Business]:
        return list(self.businesses.values())
    def update_status(self, business_id: str, status: str) -> Business | None:
        record = self.get_business(business_id)
        if record is not None: record.status = status
        return record
    def verify_business(self, business_id: str) -> Business | None:
        record = self.get_business(business_id)
        if record is not None: record.verified = True
        return record
    def delete_business(self, business_id: str) -> bool:
        return self.businesses.pop(business_id, None) is not None
