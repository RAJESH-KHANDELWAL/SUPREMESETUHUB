"""CORE facade: canonical catalogue, contracts and governance."""
from __future__ import annotations
from typing import Any
from .catalog import ECOSYSTEM_ID, list_capabilities, get_capability, catalog_status
from .governance import validate_record, publication_allowed

class GlobalCultureServiceWorkBusinessCore:
    ecosystem_id = ECOSYSTEM_ID
    def status(self) -> dict[str, Any]:
        return {"component":"CORE","status":"READY","catalogue":catalog_status(),
                "governance":"ENABLED","record_validation":"ENABLED"}
    def catalogue(self, domain: str | None = None) -> list[dict[str, Any]]:
        return list_capabilities(domain)
    def capability(self, capability_id: str) -> dict[str, Any] | None:
        return get_capability(capability_id)
    def validate(self, record: dict[str, Any]) -> list[str]:
        return validate_record(record)
    def can_publish(self, record: dict[str, Any]) -> bool:
        return publication_allowed(record)
