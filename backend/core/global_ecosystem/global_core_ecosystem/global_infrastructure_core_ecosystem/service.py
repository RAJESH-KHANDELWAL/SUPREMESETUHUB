"""CORE validation boundary for normalized infrastructure resource records."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from backend.models.infrastructure.global_infrastructure_models.validation import (
    validate_resource_record,
)


class GlobalInfrastructureCoreService:
    """Validate platform-neutral resource identity; never calls providers."""

    def describe(self) -> dict[str, Any]:
        return {
            "layer": "CORE",
            "ecosystem_id": "global-infrastructure-core-ecosystem",
            "status": "CONTRACT_VALIDATION_READY",
            "provider_operations_enabled": False,
        }

    def validate_resource(self, payload: Mapping[str, Any]) -> dict[str, Any]:
        errors = validate_resource_record(payload)
        if errors:
            return {
                "success": False,
                "error": "INFRASTRUCTURE_RESOURCE_VALIDATION_FAILED",
                "validation_errors": errors,
            }
        return {
            "success": True,
            "resource": dict(payload),
            "validated_by": "GLOBAL_INFRASTRUCTURE_CORE",
        }
