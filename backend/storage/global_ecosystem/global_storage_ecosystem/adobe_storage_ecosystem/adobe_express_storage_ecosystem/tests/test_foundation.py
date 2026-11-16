"""Offline foundation and metadata tests for ADOBE_EXPRESS_STORAGE_ECOSYSTEM."""
import pytest
from ..models import StorageObjectRecord, CategoryRecord
from ..registry import StorageMetadataRegistry
from ..service import StorageEcosystemService

def record(**overrides):
    values = {
        "provider_id": "adobe",
        "ecosystem_id": "express",
        "object_id": "sample-object",
        "name": "sample",
        "size_bytes": 10,
    }
    values.update(overrides)
    return StorageObjectRecord(**values)

def test_category_identity_and_safe_defaults():
    status = StorageEcosystemService().describe()
    assert status["ecosystem_id"] == "ADOBE_EXPRESS_STORAGE_ECOSYSTEM"
    assert status["connection_state"] == "NOT_CONFIGURED"
    assert status["provider_product_verified"] is False
    assert status["storage_operations_enabled"] is False

def test_health_does_not_claim_external_connection():
    result = StorageEcosystemService().health()
    assert result["success"] is True
    assert result["external_connection_verified"] is False
    assert result["external_connections_verified"] is False

def test_record_validation_and_registry_duplicate_guard():
    with pytest.raises(ValueError):
        record(object_id="")
    registry = StorageMetadataRegistry()
    item = record()
    registry.register(item)
    with pytest.raises(ValueError, match="DUPLICATE_OBJECT_ID"):
        registry.register(item)

def test_wrong_ecosystem_is_rejected():
    with pytest.raises(ValueError, match="RECORD_PROVIDER_OR_ECOSYSTEM_MISMATCH"):
        StorageEcosystemService().register_metadata(record(ecosystem_id="wrong"))

def test_category_metadata_model():
    item = CategoryRecord("sample-1", "Sample")
    assert item.record_type == "EXPRESS"
