"""Offline foundation tests for GOOGLE_CLOUD_STORAGE_ECOSYSTEM."""
import pytest

from ..ecosystem_models import CategoryRecord
from ..ecosystem_registry import EcosystemRegistry
from ..ecosystem_service import CategoryEcosystemService


def test_category_identity_and_safe_defaults():
    status = CategoryEcosystemService().describe()
    assert status["ecosystem_id"] == "GOOGLE_CLOUD_STORAGE_ECOSYSTEM"
    assert status["provider"] == "GOOGLE"
    assert status["category"] == "CLOUD"
    assert status["category_group"] == "DEVELOPER_AND_INFRASTRUCTURE"
    assert status["foundation_validation"] == "VALID"
    assert status["connection_state"] == "NOT_CONFIGURED"
    assert status["provider_product_verified"] is False
    assert status["storage_operations_enabled"] is False


def test_health_does_not_claim_external_connection():
    result = CategoryEcosystemService().health()
    assert result["success"] is True
    assert result["external_connection_verified"] is False


def test_registry_rejects_duplicate_record_ids():
    registry = EcosystemRegistry()
    record = CategoryRecord("record-001", "metadata sample")
    registry.register(record)
    with pytest.raises(ValueError, match="DUPLICATE_RECORD_ID"):
        registry.register(record)


def test_record_requires_non_empty_identity():
    with pytest.raises(ValueError, match="record_id and name are required"):
        CategoryRecord("", "invalid")
