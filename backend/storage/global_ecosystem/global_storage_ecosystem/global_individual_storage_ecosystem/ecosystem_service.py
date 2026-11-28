"""Validated catalog and child-package foundation service for GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM."""
import json
from pathlib import Path
from typing import Any

from .ecosystem_config import get_config, ECOSYSTEM_ID

PACKAGE_DIR = Path(__file__).resolve().parent
TAXONOMY_PATH = PACKAGE_DIR / "taxonomy" / "global_individual_storage_taxonomy.json"
INDEX_PATH = PACKAGE_DIR / "category_index.json"
MANIFEST_PATH = PACKAGE_DIR / "ecosystem_manifest.json"
SCHEMA_PATH = PACKAGE_DIR / "schemas" / "manifest.schema.json"
EXPECTED_GROUP_COUNT = 5
EXPECTED_CATEGORY_COUNT = 17

# Every child package must expose this common, offline metadata foundation.
CHILD_REQUIRED_PATHS = (
    "README.md",
    "__init__.py",
    "ecosystem_config.py",
    "ecosystem_manifest.json",
    "ecosystem_models.py",
    "ecosystem_registry.py",
    "ecosystem_service.py",
    "service.py",
    "api/routes.py",
    "models/__init__.py",
    "schemas/category_record.schema.json",
    "schemas/manifest.schema.json",
    "tests/test_foundation.py",
)


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
        """Validate root identity, taxonomy/index, package naming and all child foundations."""
        try:
            manifest = self._load_json(MANIFEST_PATH)
            taxonomy = self._load_json(TAXONOMY_PATH)
            index = self._load_json(INDEX_PATH)
            schema = self._load_json(SCHEMA_PATH)

            taxonomy_groups = taxonomy.get("categories", [])
            if not isinstance(taxonomy_groups, list):
                raise ValueError("taxonomy categories must be a list")

            taxonomy_rows = [
                {"category": category, "group": group.get("id")}
                for group in taxonomy_groups
                if isinstance(group, dict) and isinstance(group.get("items", []), list)
                for category in group.get("items", [])
            ]
            taxonomy_items = [row["category"] for row in taxonomy_rows]
            indexed_items = index.get("categories", [])
            if not isinstance(indexed_items, list):
                raise ValueError("category index categories must be a list")

            taxonomy_group_ids = [group.get("id") for group in taxonomy_groups if isinstance(group, dict)]
            taxonomy_group_map = {row["category"]: row["group"] for row in taxonomy_rows}
            child_package_checks: dict[str, bool] = {}
            child_structure_checks: dict[str, bool] = {}
            child_missing_paths: dict[str, list[str]] = {}

            for row in taxonomy_rows:
                category_id = row["category"]
                group_id = row["group"]
                package_name = f"global_individual_{str(category_id).lower()}_storage_ecosystem"
                child_dir = PACKAGE_DIR / package_name
                child_manifest_path = child_dir / "ecosystem_manifest.json"
                try:
                    child_manifest = self._load_json(child_manifest_path)
                    child_package_checks[category_id] = all((
                        child_manifest.get("ecosystem_id") == f"GLOBAL_INDIVIDUAL_{category_id}_STORAGE_ECOSYSTEM",
                        child_manifest.get("package_name") == package_name,
                        child_manifest.get("provider") == self.provider,
                        child_manifest.get("category") == category_id,
                        child_manifest.get("category_group") == group_id,
                        child_manifest.get("implementation_state") == "CATEGORY_FOUNDATION_SCAFFOLD",
                        child_manifest.get("connection_state") == "NOT_CONFIGURED",
                        child_manifest.get("provider_product_verified") is False,
                        child_manifest.get("storage_operations_enabled") is False,
                        child_manifest.get("requires_authorized_integration") is True,
                        child_manifest.get("requires_live_health_check") is True,
                        child_manifest.get("requires_end_to_end_tests") is True,
                    ))
                except (OSError, ValueError, TypeError):
                    child_package_checks[category_id] = False

                required_paths = list(CHILD_REQUIRED_PATHS) + [
                    f"php/{package_name}.php"
                ]
                missing = [relative for relative in required_paths if not (child_dir / relative).is_file()]
                child_missing_paths[category_id] = missing
                child_structure_checks[category_id] = not missing

            indexed_folder_names = [
                f"global_individual_{str(category).lower()}_storage_ecosystem"
                for category in indexed_items
            ]

            checks = {
                "manifest_ecosystem_id": manifest.get("ecosystem_id") == self.ecosystem_id,
                "manifest_package": manifest.get("package_name") == self.package_name,
                "manifest_provider": manifest.get("provider") == self.provider,
                "manifest_category": manifest.get("category") == self.category,
                "manifest_category_group": manifest.get("category_group") == self.category_group,
                "manifest_schema_identity": schema.get("properties", {}).get("ecosystem_id", {}).get("const") == self.ecosystem_id,
                "implementation_state": manifest.get("implementation_state") == "CATEGORY_FOUNDATION_SCAFFOLD",
                "taxonomy_identity": taxonomy.get("root") == self.ecosystem_id,
                "index_identity": index.get("ecosystem_id") == self.ecosystem_id,
                "taxonomy_index_match": sorted(taxonomy_items) == sorted(indexed_items),
                "expected_group_count": len(taxonomy_group_ids) == EXPECTED_GROUP_COUNT,
                "no_duplicate_groups": len(set(taxonomy_group_ids)) == len(taxonomy_group_ids),
                "expected_category_count": len(taxonomy_items) == EXPECTED_CATEGORY_COUNT,
                "index_count_match": index.get("category_count") == len(indexed_items) == EXPECTED_CATEGORY_COUNT,
                "no_duplicate_taxonomy_categories": len(set(taxonomy_items)) == len(taxonomy_items),
                "no_duplicate_index_categories": len(set(indexed_items)) == len(indexed_items),
                "folder_naming_matches": len(indexed_folder_names) == len(set(indexed_folder_names)),
                "taxonomy_group_mapping_complete": len(taxonomy_group_map) == len(taxonomy_items),
                "child_package_count_match": len(child_package_checks) == EXPECTED_CATEGORY_COUNT,
                "all_child_packages_valid": all(child_package_checks.values()) and len(child_package_checks) == EXPECTED_CATEGORY_COUNT,
                "all_child_package_structures_present": all(child_structure_checks.values()) and len(child_structure_checks) == EXPECTED_CATEGORY_COUNT,
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
                "taxonomy_group_count": len(taxonomy_group_ids),
                "taxonomy_category_count": len(taxonomy_items),
                "indexed_category_count": len(indexed_items),
                "unique_category_count": len(set(indexed_items)),
                "child_package_count": len(child_package_checks),
                "valid_child_package_count": sum(child_package_checks.values()),
                "complete_child_package_count": sum(child_structure_checks.values()),
                "child_package_checks": child_package_checks,
                "child_structure_checks": child_structure_checks,
                "child_missing_paths": child_missing_paths,
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
                "child_package_count": 0,
                "valid_child_package_count": 0,
                "complete_child_package_count": 0,
                "child_package_checks": {},
                "child_structure_checks": {},
                "child_missing_paths": {},
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
            "child_package_count": validation["child_package_count"],
            "valid_child_package_count": validation["valid_child_package_count"],
            "complete_child_package_count": validation["complete_child_package_count"],
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
