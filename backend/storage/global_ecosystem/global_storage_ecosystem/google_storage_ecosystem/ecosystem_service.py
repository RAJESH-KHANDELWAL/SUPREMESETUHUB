"""Validated catalog service for GOOGLE_STORAGE_ECOSYSTEM; never performs provider I/O."""
import json
from pathlib import Path
from typing import Any

from .ecosystem_config import ECOSYSTEM_ID, get_config

PACKAGE_DIR = Path(__file__).resolve().parent
TAXONOMY_PATH = PACKAGE_DIR / "taxonomy" / "google_storage_taxonomy.json"
INDEX_PATH = PACKAGE_DIR / "category_index.json"
MANIFEST_PATH = PACKAGE_DIR / "ecosystem_manifest.json"
SCHEMA_PATH = PACKAGE_DIR / "schemas" / "manifest.schema.json"
ROOT_PATH = "backend/storage/global_ecosystem/global_storage_ecosystem/google_storage_ecosystem/"


class EcosystemService:
    ecosystem_id = ECOSYSTEM_ID
    provider = "GOOGLE"

    def __init__(self, config: dict | None = None) -> None:
        self.config = dict(config or get_config())

    @staticmethod
    def _read_json(path: Path) -> dict[str, Any]:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
        if not isinstance(value, dict):
            raise ValueError(f"{path.name} must contain a JSON object")
        return value

    def validate_catalog(self) -> dict[str, Any]:
        """Validate identity, category sets, group mapping, naming and paths."""
        try:
            taxonomy = self._read_json(TAXONOMY_PATH)
            index = self._read_json(INDEX_PATH)
            manifest = self._read_json(MANIFEST_PATH)
            schema = self._read_json(SCHEMA_PATH)

            taxonomy_rows = [
                {"category": category, "group": group["group"]}
                for group in taxonomy.get("groups", [])
                for category in group.get("categories", [])
            ]
            folders = index.get("folders", [])
            taxonomy_categories = [row["category"] for row in taxonomy_rows]
            indexed_categories = [row.get("category") for row in folders]
            taxonomy_group_map = {row["category"]: row["group"] for row in taxonomy_rows}
            taxonomy_group_ids = [group.get("group") for group in taxonomy.get("groups", [])]
            folder_names = [row.get("folder") for row in folders]

            checks = {
                "taxonomy_identity": taxonomy.get("ecosystem_id") == ECOSYSTEM_ID,
                "index_identity": index.get("ecosystem_id") == ECOSYSTEM_ID,
                "manifest_identity": manifest.get("ecosystem_id") == ECOSYSTEM_ID,
                "schema_identity": schema.get("properties", {}).get("ecosystem_id", {}).get("const") == ECOSYSTEM_ID,
                "taxonomy_index_category_match": sorted(taxonomy_categories) == sorted(indexed_categories),
                "no_duplicate_taxonomy_categories": len(set(taxonomy_categories)) == len(taxonomy_categories),
                "no_duplicate_taxonomy_groups": len(set(taxonomy_group_ids)) == len(taxonomy_group_ids),
                "category_count_matches": index.get("category_folder_count") == len(folders) == len(taxonomy_categories),
                "no_duplicate_categories": len(set(indexed_categories)) == len(indexed_categories),
                "no_duplicate_folders": len(set(folder_names)) == len(folder_names),
                "group_mapping_matches": all(taxonomy_group_map.get(row.get("category")) == row.get("group") for row in folders),
                "folder_naming_matches": all(row.get("folder") == f"google_{str(row.get('category', '')).lower()}_storage_ecosystem" for row in folders),
                "paths_match_folder_names": all(row.get("path") == ROOT_PATH + str(row.get("folder", "")) + "/" for row in folders),
                "taxonomy_only": manifest.get("taxonomy_only") is True,
                "storage_operations_disabled": manifest.get("storage_operations_enabled") is False,
                "external_connection_unconfigured": manifest.get("external_connection_state") == "NOT_CONFIGURED",
            }
            return {
                "valid": all(checks.values()),
                "checks": checks,
                "taxonomy_group_count": len(taxonomy.get("groups", [])),
                "taxonomy_category_count": len(taxonomy_categories),
                "indexed_folder_count": len(folders),
                "unique_folder_count": len(set(folder_names)),
                "duplicate_categories": sorted({x for x in indexed_categories if indexed_categories.count(x) > 1}),
                "duplicate_folders": sorted({x for x in folder_names if folder_names.count(x) > 1}),
            }
        except (OSError, ValueError, TypeError, KeyError) as exc:
            return {
                "valid": False,
                "checks": {"catalog_files_readable": False},
                "error": str(exc),
                "taxonomy_group_count": 0,
                "taxonomy_category_count": 0,
                "indexed_folder_count": 0,
                "unique_folder_count": 0,
            }

    def describe(self) -> dict[str, Any]:
        validation = self.validate_catalog()
        return {
            "ecosystem_id": self.ecosystem_id,
            "provider": self.provider,
            "package_type": "STORAGE_TAXONOMY_AND_METADATA_FOUNDATION",
            "category_count": validation["taxonomy_category_count"],
            "indexed_folder_count": validation["indexed_folder_count"],
            "unique_folder_count": validation["unique_folder_count"],
            "catalog_validation": "VALID" if validation["valid"] else "INVALID",
            "taxonomy_only": True,
            "implementation_state": "TAXONOMY_AND_CATALOG_FOUNDATION",
            "connection_state": "NOT_CONFIGURED",
            "provider_product_verification_required": True,
            "storage_operations_enabled": False,
        }

    def health(self) -> dict[str, Any]:
        validation = self.validate_catalog()
        return {
            "success": validation["valid"],
            "status": "CATALOG_READY" if validation["valid"] else "CATALOG_INCONSISTENT",
            "external_connection_verified": False,
            "category_index_consistent": validation["valid"],
            "catalog_validation": validation,
        }
