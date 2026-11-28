"""Offline tests for the GLOBAL INTEGRATIONS storage catalog; no provider I/O."""
import pytest
from ..ecosystem_service import EcosystemService
from ..ecosystem_models import EcosystemRecord
from ..ecosystem_registry import EcosystemRegistry
from ..catalog_api import GlobalIntegrationsStorageCatalog


def test_health_does_not_claim_provider_connection():
    result = EcosystemService().health()
    assert result["success"]
    assert result["external_connections_verified"] is False
    assert result["storage_operations_enabled"] is False


def test_api_aligned_catalog_is_consistent():
    result = EcosystemService().validate_catalog()
    assert result["valid"], result
    assert result["category_count"] == 30


def test_catalog_lookup_preserves_provider_first_names():
    catalog = GlobalIntegrationsStorageCatalog()
    row = catalog.get("APPLE_INTEGRATIONS")
    assert row is not None
    assert row["storage_folder"] == "apple_integrations_storage_ecosystem"


def test_registry_duplicate_guard():
    registry = EcosystemRegistry()
    row = EcosystemRecord("sample-1", "SAMPLE", "Sample")
    registry.register(row)
    with pytest.raises(ValueError, match="DUPLICATE_RECORD_ID"):
        registry.register(row)


def test_record_requires_identity_fields():
    with pytest.raises(ValueError):
        EcosystemRecord("", "SAMPLE", "Sample")
