"""Business application service with validation and persistence."""
from __future__ import annotations
from typing import Any
from backend.database.service import DatabaseService
from .model import Business
from .repository import BusinessRepository

SUPPORTED_BUSINESS_TYPES = {
    "SMALL_BUSINESS", "MEDIUM_BUSINESS", "LARGE_BUSINESS", "ENTERPRISE",
    "STARTUP", "SOLE_PROPRIETORSHIP", "PARTNERSHIP", "LLP", "PRIVATE_LIMITED",
    "PUBLIC_LIMITED", "NON_PROFIT", "OTHER",
}

class BusinessService:
    def __init__(self, database: DatabaseService | None = None) -> None:
        self.repository = BusinessRepository(database)

    def create_business(self, *, business_id: str, owner_id: str, name: str, **values: Any) -> Business:
        if not str(owner_id).strip():
            raise ValueError("owner_id is required")
        if not str(name).strip():
            raise ValueError("name is required")
        business_type = str(values.get("business_type") or "SMALL_BUSINESS").strip().upper()
        if business_type not in SUPPORTED_BUSINESS_TYPES:
            raise ValueError(f"Unsupported business_type: {business_type}")
        employee_count = values.get("employee_count")
        if employee_count is not None and (isinstance(employee_count, bool) or int(employee_count) < 0):
            raise ValueError("employee_count must be a non-negative integer")
        payload = {
            "business_id": str(business_id).strip(), "owner_id": str(owner_id).strip(),
            "name": str(name).strip(), "category": str(values.get("category") or ""),
            "location": str(values.get("location") or ""), "website": str(values.get("website") or ""),
            "public_contact": str(values.get("public_contact") or ""), "source": str(values.get("source") or ""),
            "status": str(values.get("status") or "ACTIVE").strip().upper(),
            "verified": bool(values.get("verified", False)), "metadata": values.get("metadata") or {},
            "legal_name": str(values.get("legal_name") or ""), "business_type": business_type,
            "industry": str(values.get("industry") or ""), "employee_count": employee_count,
            "headquarters": str(values.get("headquarters") or ""),
            "parent_company_id": str(values.get("parent_company_id") or ""),
            "annual_revenue_band": str(values.get("annual_revenue_band") or ""),
            "operating_regions": values.get("operating_regions") or [],
            "departments": values.get("departments") or [], "tags": values.get("tags") or [],
            "compliance_status": str(values.get("compliance_status") or "UNSPECIFIED").strip().upper(),
        }
        if not payload["business_id"]:
            raise ValueError("business_id is required")
        return self.repository.create(payload)

    def get_business(self, business_id: str) -> Business | None:
        return self.repository.get(business_id)

    def list_businesses(self) -> list[Business]:
        return self.repository.list()

    def update_status(self, business_id: str, status: str) -> Business | None:
        normalized = str(status).strip().upper()
        if not normalized:
            raise ValueError("status is required")
        return self.repository.update_status(business_id, normalized)

    def verify_business(self, business_id: str) -> Business | None:
        return self.repository.verify(business_id)

    def delete_business(self, business_id: str) -> bool:
        return self.repository.delete(business_id)
