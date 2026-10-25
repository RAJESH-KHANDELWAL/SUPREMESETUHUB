"""Business controller for business and enterprise operations."""
from typing import Any
from backend.businesses.model import Business
from backend.businesses.service import BusinessService

class BusinessController:
    def __init__(self):
        self.service = BusinessService()

    def create(self, business_id: str, owner_id: str, name: str, category: str = "",
        location: str = "", website: str = "", public_contact: str = "", source: str = "",
        status: str = "ACTIVE", verified: bool = False, metadata: dict[str, Any] | None = None,
        legal_name: str = "", business_type: str = "SMALL_BUSINESS", industry: str = "",
        employee_count: int | None = None, headquarters: str = "", parent_company_id: str = "",
        annual_revenue_band: str = "", operating_regions: list[str] | None = None,
        departments: list[str] | None = None, tags: list[str] | None = None,
        compliance_status: str = "UNSPECIFIED") -> Business:
        return self.service.create_business(
            business_id=business_id, owner_id=owner_id, name=name, category=category,
            location=location, website=website, public_contact=public_contact, source=source,
            status=status, verified=verified, metadata=metadata, legal_name=legal_name,
            business_type=business_type, industry=industry, employee_count=employee_count,
            headquarters=headquarters, parent_company_id=parent_company_id,
            annual_revenue_band=annual_revenue_band, operating_regions=operating_regions,
            departments=departments, tags=tags, compliance_status=compliance_status)
    def get(self, business_id: str) -> Business | None:
        return self.service.get_business(business_id)
    def list(self) -> list[Business]:
        return self.service.list_businesses()
    def update_status(self, business_id: str, status: str) -> Business | None:
        return self.service.update_status(business_id=business_id, status=status)
    def verify(self, business_id: str) -> Business | None:
        return self.service.verify_business(business_id)
    def delete(self, business_id: str) -> bool:
        return self.service.delete_business(business_id)
