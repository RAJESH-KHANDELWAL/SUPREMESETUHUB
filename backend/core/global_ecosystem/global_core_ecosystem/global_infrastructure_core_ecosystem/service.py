"""Read-only infrastructure resource validation and secret-safe output."""
from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.model.global_ecosystem.global_model_ecosystem.validation import validate_resource_record

_SECRET_MARKERS = ("password", "secret", "token", "api_key", "apikey", "credential", "private_key")

def _redact(value):
    if isinstance(value, Mapping):
        return {
            key: _redact(item)
            for key, item in value.items()
            if not any(marker in str(key).lower() for marker in _SECRET_MARKERS)
        }
    if isinstance(value, list):
        return [_redact(item) for item in value]
    if isinstance(value, tuple):
        return [_redact(item) for item in value]
    return value

class GlobalInfrastructureCoreService:
    """Validate resource metadata only; never provisions or contacts providers."""

    def describe(self) -> dict:
        return {
            "ecosystem_id": "GLOBAL-INFRASTRUCTURE-CORE-ECOSYSTEM",
            "status": "READY",
            "provider_operations_enabled": False,
            "live_connections_verified": False,
        }

    def validate_resource(self, record) -> dict:
        if not isinstance(record, Mapping):
            return {"success": False, "errors": ["resource must be a mapping"], "provider_operations_enabled": False}
        errors = validate_resource_record(record)
        if errors:
            return {"success": False, "errors": errors, "provider_operations_enabled": False}
        resource = _redact(deepcopy(dict(record)))
        return {
            "success": True,
            "resource": resource,
            "errors": [],
            "validated_only": True,
            "provider_operations_enabled": False,
        }

__all__ = ["GlobalInfrastructureCoreService"]
