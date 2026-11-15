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
        """Check manifest, taxonomy and category index agree with one another."""
        try:
            manifest = self._load_json(MANIFEST_PATH)
            taxonomy = self._load_json(TAXONOMY_PATH)
            index = self._load_json(INDEX_PATH)
            taxonomy_items = [
                item
                for group in taxonomy.get("categories", [])
                for item in group.get("items", [])
            ]
            indexed_items = index.get("categories", [])
            unique_items = set(indexed_items)
            checks = {
                "manifest_identity": manifest.get("ecosystem_id") == ECOSYSTEM_ID,
                "manifest_category": manifest.get("category") == self.category,
                "manifest_group": manifest.get("category_group") == self.category_group,
                "taxonomy_identity": taxonomy.get("root") == ECOSYSTEM_ID,
                "index_identity": index.get("ecosystem_id") == ECOSYSTEM_ID,
                "taxonomy_index_match": sorted(taxonomy_items) == sorted(indexed_items),
                "index_count_match": index.get("category_count") == len(indexed_items),
                "no_duplicate_categories": len(unique_items) == len(indexed_items),
                "operations_disabled": manifest.get("storage_operations_enabled") is False,
                "connection_unconfigured": manifest.get("connection_state") == "NOT_CONFIGURED",
            }
            return {
                "valid": all(checks.values()),
                "checks": checks,
                "taxonomy_category_count": len(taxonomy_items),
                "indexed_category_count": len(indexed_items),
                "unique_category_count": len(unique_items),
            }
        except (OSError, ValueError, TypeError, KeyError) as exc:
            return {
                "valid": False,
                "checks": {"catalog_files_readable": False},
                "error": str(exc),
                "taxonomy_category_count": 0,
                "indexed_category_count": 0,
                "unique_category_count": 0,
            }

    def describe(self) -> dict[str, Any]:
        validation = self.validate_catalog()
        return {
            "ecosystem_id": self.ecosystem_id,
            "provider": "GLOBAL_INDIVIDUAL",
            "category": self.category,
            "category_group": self.category_group,
            "implementation_state": "CATEGORY_FOUNDATION_SCAFFOLD",
            "catalog_validation": "VALID" if validation["valid"] else "INVALID",
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


# Preserve the earlier service import while standardizing the category contract.
EcosystemService = CategoryEcosystemService
