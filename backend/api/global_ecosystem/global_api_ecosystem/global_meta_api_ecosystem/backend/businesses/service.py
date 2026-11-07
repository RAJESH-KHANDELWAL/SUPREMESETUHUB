"""Business domain service for business and enterprise profiles."""
from __future__ import annotations

from typing import Any

from backend.businesses.connection import BusinessRepository
from backend.businesses.model import Business
from backend.database.service import DatabaseService


class BusinessService:
    """Coordinates validated Business operations over persistent storage."""

    ALLOWED_TYPES = {
        "SOLE_PROPRIETORSHIP", "SMALL_BUSINESS", "MEDIUM_BUSINESS",
        "LARGE_BUSINESS", "ENTERPRISE", "NONPROFIT", "PUBLIC_SECTOR",
    }
    ALLOWED_STATUSES = {"ACTIVE", "INACTIVE", "SUSPENDED", "PENDING", "ARCHIVED"}
    ALLOWED_COMPLIANCE_STATUSES = {
        "UNSPECIFIED", "UNDER_REVIEW", "COMPLIANT", "NON_COMPLIANT", "EXEMPT",
    }

    def __init__(
        self,
        database_service: DatabaseService | None = None,
        repository: BusinessRepository | None = None,
    ) -> None:
        self.repository = repository or BusinessRepository(database_service)

    @property
    def businesses(self) -> dict[str, Business]:
        """Compatibility view for legacy callers; storage remains repository-backed."""
        return {record.business_id: record for record in self.repository.list()}

    def create_business(
        self, business_id: str, owner_id: str, name: str,
        category: str = "", location: str = "", website: str = "",
        public_contact: str = "", source: str = "", status: str = "ACTIVE",
        verified: bool = False, metadata: dict[str, Any] | None = None,
        legal_name: str = "", business_type: str = "SMALL_BUSINESS",
        industry: str = "", employee_count: int | None = None,
        headquarters: str = "", parent_company_id: str = "",
        annual_revenue_band: str = "", operating_regions: list[str] | None = None,
        departments: list[str] | None = None, tags: list[str] | None = None,
        compliance_status: str = "UNSPECIFIED",
    ) -> Business:
        business_id = business_id.strip()
        owner_id = owner_id.strip()
        name = name.strip()
        if not business_id:
            raise ValueError("business_id is required")
        if not owner_id:
            raise ValueError("owner_id is required")
        if not name:
            raise ValueError("name is required")
        if self.repository.get(business_id) is not None:
            raise ValueError(f"Business already exists: {business_id}")

        normalized_type = business_type.strip().upper() or "SMALL_BUSINESS"
        if normalized_type not in self.ALLOWED_TYPES:
            raise ValueError("Unsupported business_type")
        normalized_status = status.strip().upper() or "ACTIVE"
        if normalized_status not in self.ALLOWED_STATUSES:
            raise ValueError("Unsupported business status")
        normalized_compliance = compliance_status.strip().upper() or "UNSPECIFIED"
        if normalized_compliance not in self.ALLOWED_COMPLIANCE_STATUSES:
            raise ValueError("Unsupported compliance_status")
        if employee_count is not None and employee_count < 0:
            raise ValueError("employee_count cannot be negative")

        record = Business(
            business_id=business_id, owner_id=owner_id, name=name,
            category=category, location=location, website=website,
            public_contact=public_contact, source=source, status=normalized_status,
            verified=bool(verified), metadata=dict(metadata or {}), legal_name=legal_name,
            business_type=normalized_type, industry=industry,
            employee_count=employee_count, headquarters=headquarters,
            parent_company_id=parent_company_id, annual_revenue_band=annual_revenue_band,
            operating_regions=list(operating_regions or []),
            departments=list(departments or []), tags=list(tags or []),
            compliance_status=normalized_compliance,
        )
        return self.repository.create(record)

    def get_business(self, business_id: str) -> Business | None:
        return self.repository.get(business_id)

    def list_businesses(self) -> list[Business]:
        return self.repository.list()

    def update_status(self, business_id: str, status: str) -> Business | None:
        record = self.get_business(business_id)
        if record is None:
            return None
        normalized = status.strip().upper()
        if normalized not in self.ALLOWED_STATUSES:
            raise ValueError("Unsupported business status")
        record.status = normalized
        return self.repository.update(record)

    def verify_business(self, business_id: str) -> Business | None:
        record = self.get_business(business_id)
        if record is None:
            return None
        record.verified = True
        return self.repository.update(record)

    def delete_business(self, business_id: str) -> bool:
        return self.repository.delete(business_id)
