"""Validated foundation service for GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM."""
import json
from pathlib import Path
from typing import Any

from .ecosystem_config import get_config, ECOSYSTEM_ID


PACKAGE_DIR = Path(__file__).resolve().parent
TAXONOMY_PATH = PACKAGE_DIR / "taxonomy" / "global_individual_storage_taxonomy.json"
INDEX_PATH = PACKAGE_DIR / "category_index.json"
MANIFEST_PATH = PACKAGE_DIR / "ecosystem_manifest.json"


class CategoryEcosystemService:
    ecosystem_id = ECOSYSTEM_ID
    package_name = "global_individual_storage_ecosystem"
    provider = "GLOBAL_INDIVIDUAL"
    category = "INDIVIDUAL"
    category_group = "PERSONAL_AND_INDIVIDUAL_STORAGE"

    def __init__(self, config: dict | None = None) -> None:
        self.config = dict(config or get_config())

    @staticmethod
    def _load_json(path: Path) -> dict[str, Any]:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
        if not isinstance(value, dict):
            raise ValueError(f"Expected a JSON object in {path.name}")
        return value

    def validate_catalog(self) -> dict[str, Any]:
        """Validate canonical identity, catalog integrity and disabled operations."""
        try:
            manifest = self._load_json(MANIFEST_PATH)
            taxonomy = self._load_json(TAXONOMY_PATH)
            index = self._load_json(INDEX_PATH)
            taxonomy_groups = taxonomy.get("categories", [])
            taxonomy_items = [
                item
                for group in taxonomy_groups
                for item in group.get("items", [])
            ]
            indexed_items = index.get("categories", [])
            unique_items = set(indexed_items)
            checks = {
                "manifest_ecosystem_id": manifest.get("ecosystem_id") == self.ecosystem_id,
                "manifest_package": manifest.get("package_name") == self.package_name,
                "manifest_provider": manifest.get("provider") == self.provider,
                "manifest_category": manifest.get("category") == self.category,
                "manifest_category_group": manifest.get("category_group") == self.category_group,
                "implementation_state": manifest.get("implementation_state") == "CATEGORY_FOUNDATION_SCAFFOLD",
                "taxonomy_identity": taxonomy.get("root") == self.ecosystem_id,
                "index_identity": index.get("ecosystem_id") == self.ecosystem_id,
                "taxonomy_index_match": sorted(taxonomy_items) == sorted(indexed_items),
                "index_count_match": index.get("category_count") == len(indexed_items),
                "no_duplicate_categories": len(unique_items) == len(indexed_items),
                "connection_unconfigured": manifest.get("connection_state") == "NOT_CONFIGURED",
                "provider_product_unverified": manifest.get("provider_product_verified") is False,
                "operations_disabled": manifest.get("storage_operations_enabled") is False,
                "authorized_integration_required": manifest.get("requires_authorized_integration") is True,
                "live_health_check_required": manifest.get("requires_live_health_check") is True,
                "end_to_end_tests_required": manifest.get("requires_end_to_end_tests") is True,
            }
            return {
                "valid": all(checks.values()),
                "checks": checks,
                "taxonomy_group_count": len(taxonomy_groups),
                "taxonomy_category_count": len(taxonomy_items),
                "indexed_category_count": len(indexed_items),
                "unique_category_count": len(unique_items),
            }
        except (OSError, ValueError, TypeError, KeyError) as exc:
            return {
                "valid": False,
                "checks": {"catalog_files_readable": False},
                "error": str(exc),
                "taxonomy_group_count": 0,
                "taxonomy_category_count": 0,
                "indexed_category_count": 0,
                "unique_category_count": 0,
            }

    def describe(self) -> dict[str, Any]:
        validation = self.validate_catalog()
        return {
            "ecosystem_id": self.ecosystem_id,
            "package_name": self.package_name,
            "provider": self.provider,
            "category": self.category,
            "category_group": self.category_group,
            "implementation_state": "CATEGORY_FOUNDATION_SCAFFOLD",
            "catalog_validation": "VALID" if validation["valid"] else "INVALID",
            "taxonomy_group_count": validation["taxonomy_group_count"],
            "taxonomy_category_count": validation["taxonomy_category_count"],
            "connection_state": "NOT_CONFIGURED",
            "provider_product_verified": False,
            "storage_operations_enabled": False,
        }

    def health(self) -> dict[str, Any]:
        validation = self.validate_catalog()
        return {
            "success": validation["valid"],
            "status": "FOUNDATION_READY" if validation["valid"] else "FOUNDATION_INVALID",
            "external_connection_verified": False,
            "storage_operations_enabled": False,
            "catalog_validation": validation,
        }


EcosystemService = CategoryEcosystemService
