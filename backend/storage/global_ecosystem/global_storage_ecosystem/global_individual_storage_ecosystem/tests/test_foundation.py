"""Offline tests for GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM."""
import pytest
from ..ecosystem_service import CategoryEcosystemService
from ..ecosystem_models import CategoryRecord
from ..ecosystem_registry import EcosystemRegistry
from ..service import GlobalIndividualStorageEcosystem


def test_health_does_not_claim_provider_connection():
    result = CategoryEcosystemService().health()
    assert result["success"] is True
    assert result["status"] == "FOUNDATION_READY"
    assert result["external_connection_verified"] is False


def test_description_reports_category_and_disabled_operations():
    result = GlobalIndividualStorageEcosystem().describe()
    assert result["ecosystem_id"] == "GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM"
    assert result["category"] == "INDIVIDUAL"
    assert result["connection_state"] == "NOT_CONFIGURED"
    assert result["storage_operations_enabled"] is False


def test_registry_register_and_duplicate_guard():
    registry = EcosystemRegistry()
    record = CategoryRecord("opaque-001", "Sample", owner_ref="owner-ref-001")
    registry.register(record)
    assert registry.get("opaque-001")["name"] == "Sample"
    with pytest.raises(ValueError, match="DUPLICATE_RECORD_ID"):
        registry.register(record)


def test_record_requires_opaque_owner_reference():
    with pytest.raises(ValueError, match="owner_ref"):
        CategoryRecord("opaque-002", "Sample")
