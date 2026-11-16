"""Offline tests for GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM root and child packages."""
import json
from pathlib import Path

import pytest

from ..ecosystem_service import CategoryEcosystemService
from ..ecosystem_models import CategoryRecord
from ..ecosystem_registry import EcosystemRegistry
from ..service import GlobalIndividualStorageEcosystem


PACKAGE_DIR = Path(__file__).resolve().parents[1]


def test_category_identity_and_safe_defaults():
    result = GlobalIndividualStorageEcosystem().describe()
    assert result["ecosystem_id"] == "GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM"
    assert result["provider"] == "GLOBAL_INDIVIDUAL"
    assert result["category"] == "INDIVIDUAL"
    assert result["category_group"] == "PERSONAL_AND_INDIVIDUAL_STORAGE"
    assert result["connection_state"] == "NOT_CONFIGURED"
    assert result["provider_product_verified"] is False
    assert result["storage_operations_enabled"] is False


def test_health_validates_root_taxonomy_index_and_all_17_child_packages():
    result = CategoryEcosystemService().health()
    assert result["success"] is True
    assert result["status"] == "FOUNDATION_READY"
    assert result["external_connection_verified"] is False
    assert result["storage_operations_enabled"] is False

    validation = result["catalog_validation"]
    assert validation["taxonomy_group_count"] == 5
    assert validation["taxonomy_category_count"] == 17
    assert validation["indexed_category_count"] == 17
    assert validation["unique_category_count"] == 17
    assert validation["child_package_count"] == 17
    assert validation["valid_child_package_count"] == 17
    assert validation["complete_child_package_count"] == 17
    assert all(validation["checks"].values())
    assert all(validation["child_package_checks"].values())
    assert all(validation["child_structure_checks"].values())
    assert all(not missing for missing in validation["child_missing_paths"].values())


def test_taxonomy_has_the_five_declared_groups_and_seventeen_categories():
    taxonomy = json.loads(
        (PACKAGE_DIR / "taxonomy" / "global_individual_storage_taxonomy.json").read_text(encoding="utf-8")
    )
    groups = taxonomy["categories"]
    categories = [item for group in groups for item in group["items"]]
    assert len(groups) == 5
    assert len(categories) == 17
    assert len(set(categories)) == 17


def test_manifest_and_schemas_are_valid_json_and_aligned():
    manifest = json.loads((PACKAGE_DIR / "ecosystem_manifest.json").read_text(encoding="utf-8"))
    manifest_schema = json.loads((PACKAGE_DIR / "schemas" / "manifest.schema.json").read_text(encoding="utf-8"))
    category_schema = json.loads((PACKAGE_DIR / "schemas" / "category_record.schema.json").read_text(encoding="utf-8"))
    individual_schema = json.loads((PACKAGE_DIR / "schemas" / "individual_storage_record.schema.json").read_text(encoding="utf-8"))
    assert manifest["ecosystem_id"] == manifest_schema["properties"]["ecosystem_id"]["const"]
    assert manifest["package_name"] == manifest_schema["properties"]["package_name"]["const"]
    assert manifest["provider"] == manifest_schema["properties"]["provider"]["const"]
    assert manifest["category"] == manifest_schema["properties"]["category"]["const"]
    assert manifest["category_group"] == manifest_schema["properties"]["category_group"]["const"]
    assert manifest["taxonomy_file"] == "taxonomy/global_individual_storage_taxonomy.json"
    assert manifest["category_index_file"] == "category_index.json"
    assert manifest["storage_operations_enabled"] is False
    assert category_schema["properties"]["record_type"]["const"] == "INDIVIDUAL"
    assert "owner_ref" in category_schema["required"]
    assert "owner_ref" in individual_schema["required"]


def test_record_requires_opaque_owner_reference():
    with pytest.raises(ValueError, match="owner_ref"):
        CategoryRecord("opaque-002", "Sample")


def test_record_rejects_blank_opaque_owner_reference():
    with pytest.raises(ValueError, match="owner_ref"):
        CategoryRecord("opaque-003", "Sample", owner_ref="   ")


def test_record_rejects_wrong_record_type():
    with pytest.raises(ValueError, match="record_type"):
        CategoryRecord("opaque-004", "Sample", record_type="OTHER", owner_ref="opaque-owner")


def test_record_rejects_empty_identifiers():
    with pytest.raises(ValueError, match="record_id and name"):
        CategoryRecord("", "Sample", owner_ref="opaque-owner")


def test_registry_register_get_and_duplicate_guard():
    registry = EcosystemRegistry()
    record = CategoryRecord("opaque-001", "Sample", owner_ref="owner-ref-001")
    registry.register(record)
    assert registry.get("opaque-001")["name"] == "Sample"
    assert len(registry.list()) == 1
    with pytest.raises(ValueError, match="DUPLICATE_RECORD_ID"):
        registry.register(record)
