"""Offline foundation tests for GLOBAL_INDIVIDUAL_PERSONAL_PHOTO_AND_VIDEO_STORAGE_STORAGE_ECOSYSTEM."""
import pytest

from ..ecosystem_models import CategoryRecord
from ..ecosystem_registry import EcosystemRegistry
from ..ecosystem_service import CategoryEcosystemService


def test_category_identity_and_safe_defaults():
    service = CategoryEcosystemService()
    status = service.describe()
    assert status["ecosystem_id"] == "GLOBAL_INDIVIDUAL_PERSONAL_PHOTO_AND_VIDEO_STORAGE_STORAGE_ECOSYSTEM"
    assert status["provider"] == "GLOBAL_INDIVIDUAL"
    assert status["category"] == "PERSONAL_PHOTO_AND_VIDEO_STORAGE"
    assert status["category_group"] == "PERSONAL_CONTENT"
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
    record = CategoryRecord("record-001", "metadata sample", owner_ref="opaque-owner-001")
    registry.register(record)
    with pytest.raises(ValueError, match="DUPLICATE_RECORD_ID"):
        registry.register(record)


def test_record_requires_opaque_owner_reference():
    with pytest.raises(ValueError, match="opaque owner_ref is required"):
        CategoryRecord("record-001", "metadata sample")


def test_record_rejects_wrong_category_type():
    with pytest.raises(ValueError, match="record_type must be PERSONAL_PHOTO_AND_VIDEO_STORAGE"):
        CategoryRecord("record-001", "metadata sample", record_type="WRONG", owner_ref="opaque-owner-001")
