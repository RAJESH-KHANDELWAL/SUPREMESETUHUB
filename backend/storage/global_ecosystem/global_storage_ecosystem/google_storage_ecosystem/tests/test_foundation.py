"""Offline tests for the Google storage taxonomy/catalog root."""
import pytest
from ..ecosystem_models import EcosystemRecord
from ..ecosystem_registry import EcosystemRegistry
from ..ecosystem_service import EcosystemService
from ..service import GoogleStorageEcosystem


def test_root_identity_is_google_storage_ecosystem():
    result = GoogleStorageEcosystem().describe()
    assert result["ecosystem_id"] == "GOOGLE_STORAGE_ECOSYSTEM"
    assert result["provider"] == "GOOGLE"
    assert result["taxonomy_only"] is True
    assert result["storage_operations_enabled"] is False


def test_taxonomy_and_index_have_unique_matching_folder_count():
    result = EcosystemService().describe()
    assert result["category_count"] == 184
    assert result["indexed_folder_count"] == 184
    assert result["unique_folder_count"] == 184


def test_health_reports_catalog_consistency_not_provider_connection():
    result = EcosystemService().health()
    assert result["success"] is True
    assert result["external_connection_verified"] is False


def test_registry_duplicate_guard():
    registry = EcosystemRegistry()
    row = EcosystemRecord("category-001", "DRIVE", "Drive")
    registry.register(row)
    with pytest.raises(ValueError, match="DUPLICATE_RECORD_ID"):
        registry.register(row)
