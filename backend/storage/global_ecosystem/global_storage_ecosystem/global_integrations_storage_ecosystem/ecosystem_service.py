"""Provider-neutral catalog foundation; deliberately performs no provider I/O."""
import json
from pathlib import Path
from typing import Any

from .ecosystem_config import ECOSYSTEM_ID, get_config
from .ecosystem_models import EcosystemRecord

PACKAGE_ID = "global_integrations_storage_ecosystem"
PACKAGE_DIR = Path(__file__).resolve().parent
MANIFEST_PATH = PACKAGE_DIR / "ecosystem_manifest.json"


class EcosystemService:
    ecosystem_id = ECOSYSTEM_ID
    package_id = PACKAGE_ID

    def __init__(self, *, config: dict | None = None):
        self.config = dict(config if config is not None else get_config())
        # Runtime enablement never implies an external connection or storage permission.
        self.enabled = bool(self.config.get("enabled", False))

    @staticmethod
    def _read_manifest() -> dict[str, Any]:
        with MANIFEST_PATH.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
        if not isinstance(value, dict):
            raise ValueError("ecosystem manifest must be a JSON object")
        return value

    def validate_manifest(self) -> dict[str, Any]:
        try:
            manifest = self._read_manifest()
            checks = {
                "canonical_ecosystem_id": manifest.get("ecosystem_id") == self.ecosystem_id,
                "canonical_provider": manifest.get("provider") == "GLOBAL INTEGRATIONS",
                "taxonomy_only": manifest.get("taxonomy_only") is True,
                "foundation_state": manifest.get("implementation_state") == "FOUNDATION_INITIALIZED",
                "external_connection_unconfigured": manifest.get("external_connection_state") == "NOT_CONFIGURED",
                "authorized_credentials_required": manifest.get("requires_authorized_credentials") is True,
                "live_health_check_required": manifest.get("requires_live_health_check") is True,
                "end_to_end_tests_required": manifest.get("requires_end_to_end_tests") is True,
            }
            return {"valid": all(checks.values()), "checks": checks}
        except (OSError, ValueError, TypeError) as exc:
            return {"valid": False, "checks": {"manifest_readable": False}, "error": str(exc)}

    def describe(self) -> dict:
        validation = self.validate_manifest()
        return {
            "ecosystem_id": self.ecosystem_id,
            "package": self.package_id,
            "enabled": self.enabled,
            "implementation_state": "FOUNDATION_INITIALIZED",
            "foundation_validation": "VALID" if validation["valid"] else "INVALID",
            "external_connection_state": "NOT_CONFIGURED",
            "external_connections_verified": False,
            "taxonomy_only": True,
            "storage_operations_enabled": False,
            "responsibility": [
                "STORAGE_SIDE_IDENTITY",
                "METADATA",
                "TAXONOMY",
                "OBJECT_LIFECYCLE_DEFINITIONS",
                "STORAGE_HEALTH_METADATA",
            ],
            "capabilities": ["IDENTITY", "CONFIGURATION", "METADATA", "HEALTH_CONTRACT"],
        }

    def health(self) -> dict:
        validation = self.validate_manifest()
        valid = validation["valid"]
        return {
            "success": valid,
            "ecosystem_id": self.ecosystem_id,
            "status": "FOUNDATION_READY" if valid else "FOUNDATION_INVALID",
            "foundation_validation": validation,
            "external_connections_verified": False,
            "storage_operations_enabled": False,
        }

    @staticmethod
    def serialize_record(record: EcosystemRecord) -> dict:
        from dataclasses import asdict
        return asdict(record)
