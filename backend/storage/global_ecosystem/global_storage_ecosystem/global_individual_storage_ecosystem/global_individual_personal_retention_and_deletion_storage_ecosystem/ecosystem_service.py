"""Validated foundation service for GLOBAL_INDIVIDUAL_PERSONAL_RETENTION_AND_DELETION_STORAGE_ECOSYSTEM; external operations remain disabled."""
import json
from pathlib import Path
from typing import Any

from .ecosystem_config import ECOSYSTEM_ID, get_config

PACKAGE_DIR = Path(__file__).resolve().parent
MANIFEST_PATH = PACKAGE_DIR / "ecosystem_manifest.json"


class CategoryEcosystemService:
    ecosystem_id = ECOSYSTEM_ID
    package_name = "global_individual_personal_retention_and_deletion_storage_ecosystem"
    provider = "GLOBAL_INDIVIDUAL"
    category = "PERSONAL_RETENTION_AND_DELETION"
    category_group = "DATA_RIGHTS_AND_LIFECYCLE"

    def __init__(self, config: dict | None = None) -> None:
        self.config = dict(config or get_config())

    def validate_manifest(self) -> dict[str, Any]:
        try:
            with MANIFEST_PATH.open("r", encoding="utf-8") as handle:
                manifest = json.load(handle)
            checks = {
                "ecosystem_identity": manifest.get("ecosystem_id") == self.ecosystem_id,
                "package_identity": manifest.get("package_name") == self.package_name,
                "provider_identity": manifest.get("provider") == self.provider,
                "category_identity": manifest.get("category") == self.category,
                "category_group_identity": manifest.get("category_group") == self.category_group,
                "foundation_state": manifest.get("implementation_state") == "CATEGORY_FOUNDATION_SCAFFOLD",
                "connection_unconfigured": manifest.get("connection_state") == "NOT_CONFIGURED",
                "provider_unverified": manifest.get("provider_product_verified") is False,
                "storage_operations_disabled": manifest.get("storage_operations_enabled") is False,
                "authorized_integration_required": manifest.get("requires_authorized_integration") is True,
                "live_health_check_required": manifest.get("requires_live_health_check") is True,
                "end_to_end_tests_required": manifest.get("requires_end_to_end_tests") is True,
            }
            return {"valid": all(checks.values()), "checks": checks}
        except (OSError, ValueError, TypeError) as exc:
            return {"valid": False, "checks": {"manifest_readable": False}, "error": str(exc)}

    def describe(self) -> dict[str, Any]:
        validation = self.validate_manifest()
        return {
            "ecosystem_id": self.ecosystem_id,
            "provider": self.provider,
            "category": self.category,
            "category_group": self.category_group,
            "implementation_state": "CATEGORY_FOUNDATION_SCAFFOLD",
            "foundation_validation": "VALID" if validation["valid"] else "INVALID",
            "connection_state": "NOT_CONFIGURED",
            "provider_product_verified": False,
            "storage_operations_enabled": False,
        }

    def health(self) -> dict[str, Any]:
        validation = self.validate_manifest()
        return {
            "success": validation["valid"],
            "status": "FOUNDATION_READY" if validation["valid"] else "FOUNDATION_INCONSISTENT",
            "external_connection_verified": False,
            "storage_operations_enabled": False,
            "validation": validation,
        }
