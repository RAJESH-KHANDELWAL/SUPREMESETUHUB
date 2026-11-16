"""Domain service for Bada Business program discovery and validation."""

from .policies import normalize_program_id, validate_enrollment_request
from .resource_adapter import BadaBusinessProgramResourceAdapter


class BadaBusinessProgramsService:
    def __init__(self, resource_adapter=None):
        self.resource_adapter = resource_adapter or BadaBusinessProgramResourceAdapter()

    def list_programs(self):
        programs = self.resource_adapter.list_programs()
        return {"success": True, "count": len(programs), "programs": programs}

    def get_program(self, program_id: str):
        key = normalize_program_id(program_id)
        program = self.resource_adapter.get_program(key)
        if program is None:
            return {"success": False, "error": "PROGRAM_NOT_FOUND", "program_id": key}
        return {"success": True, "program": program}

    def search_programs(self, query: str):
        if not isinstance(query, str) or not query.strip():
            raise ValueError("query must be a non-empty string")
        term = query.strip().casefold()
        matches = [
            item for item in self.resource_adapter.list_programs()
            if term in str(item.get("name", "")).casefold()
            or term in str(item.get("program_id", "")).casefold()
            or term in str(item.get("tagline", "")).casefold()
        ]
        return {"success": True, "count": len(matches), "programs": matches}

    def prepare_enrollment_request(self, program_id: str, applicant: dict):
        result = self.get_program(program_id)
        if not result["success"]:
            return result
        request = validate_enrollment_request(result["program"], applicant)
        return {"success": True, "request": request}

    def get_status(self):
        catalog = self.resource_adapter.get_catalog()
        return {
            "success": True,
            "ecosystem_id": "BADA-BUSINESS-CORE-PROGRAMS",
            "layer": "CORE",
            "status": "READY",
            "program_count": catalog.get("program_count", 0),
            "canonical_source": "backend.global_ecosystem.global_bada_business_ecosystem.platform_resources.catalog",
            "live_registration_enabled": False,
            "payment_processing_enabled": False,
        }
