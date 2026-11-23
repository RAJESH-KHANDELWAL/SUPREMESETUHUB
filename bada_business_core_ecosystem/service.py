"""Read-only Bada Business CORE control-plane service."""
from __future__ import annotations
from typing import Any
from .policies import ensure_operation_is_catalog_only, registration_readiness
from .resource_adapter import BadaBusinessResourceAdapter

class BadaBusinessCoreService:
    def __init__(self, adapter: BadaBusinessResourceAdapter | None = None) -> None:
        self.adapter = adapter or BadaBusinessResourceAdapter()

    def status(self) -> dict[str, Any]:
        catalog = self.adapter.catalog()
        return {"success": True, "ecosystem_id": "BADA-BUSINESS-CORE-ECOSYSTEM", "layer": "CORE", "status": "RESOURCE_CATALOG_CONNECTED", "provider": catalog.get("platform", {}).get("provider", "Bada Business"), "program_count": catalog.get("program_count", 0), "platform_link_count": catalog.get("link_count", 0), "course_count": len(self.adapter.courses()), "event_count": len(self.adapter.events()), "product_count": len(self.adapter.products()), "official_public_api_verified": catalog.get("official_public_api_verified", False), "live_connection_verified": catalog.get("live_connection_verified", False), "registration": registration_readiness()}

    def list_programs(self) -> dict[str, Any]:
        records = self.adapter.programs()
        return {"success": True, "count": len(records), "programs": records}

    def get_program(self, program_id: str) -> dict[str, Any]:
        record = self.adapter.program(program_id.strip().lower())
        return {"success": record is not None, "program": record, **({} if record else {"error": "PROGRAM_NOT_FOUND"})}

    def list_courses(self) -> dict[str, Any]:
        records = self.adapter.courses()
        return {"success": True, "count": len(records), "courses": list(records)}

    def search_courses(self, query: str) -> dict[str, Any]:
        if not isinstance(query, str) or not query.strip(): raise ValueError("QUERY_REQUIRED")
        records = self.adapter.search_courses(query)
        return {"success": True, "count": len(records), "courses": list(records)}

    def list_events(self) -> dict[str, Any]:
        records = self.adapter.events()
        return {"success": True, "count": len(records), "events": list(records)}

    def list_links(self) -> dict[str, Any]:
        records = self.adapter.links()
        return {"success": True, "count": len(records), "links": records}

    def list_products(self) -> dict[str, Any]:
        records = self.adapter.products()
        return {"success": True, "count": len(records), "products": records, "status": "NO_CANONICAL_PRODUCT_RECORDS_PUBLISHED" if not records else "CATALOG_ONLY"}

    def validate_registration(self, payload: dict[str, Any]) -> dict[str, Any]:
        errors = self.adapter.validate_registration(payload)
        return {"success": not errors, "status": "VALIDATION_ONLY" if not errors else "INVALID_INPUT", "errors": errors, "registration_submitted": False, "payment_processed": False}

    def referral_code(self, url: str) -> dict[str, Any]:
        return {"success": True, "referral_code": self.adapter.referral_code(url)}

    def request_operation(self, operation: str) -> dict[str, Any]:
        ensure_operation_is_catalog_only(operation)
        return {"success": True, "operation": operation, "mode": "CATALOG_ONLY"}
