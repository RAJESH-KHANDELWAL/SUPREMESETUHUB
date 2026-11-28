"""Validated API-aligned catalog service; never performs provider I/O."""
import json
from pathlib import Path
from typing import Any
from .ecosystem_config import get_config

PACKAGE_ID = "global_integrations_storage_ecosystem"
ECOSYSTEM_ID = "GLOBAL_INTEGRATIONS_STORAGE_ECOSYSTEM"
PACKAGE_DIR = Path(__file__).resolve().parent
TAXONOMY_PATH = PACKAGE_DIR / "taxonomy" / "global_integrations_storage_taxonomy.json"
INDEX_PATH = PACKAGE_DIR / "category_index.json"
MANIFEST_PATH = PACKAGE_DIR / "ecosystem_manifest.json"
SCHEMA_PATH = PACKAGE_DIR / "schemas" / "manifest.schema.json"

class EcosystemService:
    def __init__(self, *, config: dict | None = None):
        self.config = dict(config or get_config())
        self.enabled = bool(self.config.get("enabled", True))

    @staticmethod
    def _read_json(path: Path) -> dict[str, Any]:
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise ValueError(f"{path.name} must contain a JSON object")
        return value

    def validate_catalog(self) -> dict[str, Any]:
        try:
            taxonomy = self._read_json(TAXONOMY_PATH)
            index = self._read_json(INDEX_PATH)
            manifest = self._read_json(MANIFEST_PATH)
            schema = self._read_json(SCHEMA_PATH)
            rows = [row for group in taxonomy.get("groups", []) for row in group.get("categories", [])]
            folders = index.get("folders", [])
            names = [row.get("folder") for row in folders]
            categories = [row.get("category") for row in folders]
            checks = {
                "taxonomy_identity": taxonomy.get("ecosystem_id") == ECOSYSTEM_ID,
                "index_identity": index.get("ecosystem_id") == ECOSYSTEM_ID,
                "manifest_identity": manifest.get("ecosystem_id") == ECOSYSTEM_ID,
                "schema_identity": schema.get("properties", {}).get("ecosystem_id", {}).get("const") == ECOSYSTEM_ID,
                "taxonomy_index_category_match": sorted(row.get("category") for row in rows) == sorted(categories),
                "no_duplicate_categories": len(set(categories)) == len(categories),
                "no_duplicate_folders": len(set(names)) == len(names),
                "category_count_matches": index.get("category_folder_count") == len(folders) == manifest.get("category_folder_count"),
                "api_source_names_preserved": all(str(row.get("source_api_folder", "")).endswith("_api_ecosystem") for row in folders),
                "storage_folder_names_valid": all(str(row.get("folder", "")).endswith("_storage_ecosystem") for row in folders),
                "child_scaffolds_exist": all((PACKAGE_DIR / str(row.get("folder", "")) / "README.md").is_file() for row in folders),
                "taxonomy_only": manifest.get("taxonomy_only") is True,
                "storage_operations_disabled": manifest.get("storage_operations_enabled") is False,
                "external_connection_unconfigured": manifest.get("external_connection_state") == "NOT_CONFIGURED",
            }
            return {"valid": all(checks.values()), "checks": checks, "category_count": len(categories), "unique_folder_count": len(set(names))}
        except (OSError, ValueError, TypeError, KeyError) as exc:
            return {"valid": False, "checks": {"catalog_files_readable": False}, "error": str(exc), "category_count": 0, "unique_folder_count": 0}

    def describe(self) -> dict[str, Any]:
        result = self.validate_catalog()
        return {"ecosystem_id": ECOSYSTEM_ID, "package": PACKAGE_ID, "provider": "GLOBAL INTEGRATIONS", "owner_layer": "STORAGE", "enabled": self.enabled, "package_type": "API_ALIGNED_STORAGE_TAXONOMY_AND_METADATA_FOUNDATION", "category_count": result["category_count"], "catalog_validation": "VALID" if result["valid"] else "INVALID", "implementation_state": "TAXONOMY_AND_CATALOG_FOUNDATION", "connection_state": "NOT_CONFIGURED", "external_connections_verified": False, "storage_operations_enabled": False}

    def health(self) -> dict[str, Any]:
        result = self.validate_catalog()
        return {"success": result["valid"], "ecosystem_id": ECOSYSTEM_ID, "status": "CATALOG_READY" if result["valid"] else "CATALOG_INCONSISTENT", "external_connections_verified": False, "storage_operations_enabled": False, "catalog_validation": result}

    def serialize_record(self, record) -> dict:
        from dataclasses import asdict
        return asdict(record)
