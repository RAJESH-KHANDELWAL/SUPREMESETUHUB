"""Offline contract tests; no network or provider credentials required."""
from ..ecosystem_service import CategoryEcosystemService
from ..ecosystem_models import CategoryRecord

def test_foundation_is_not_connected():
    service = CategoryEcosystemService()
    assert service.describe()["connection_state"] == "NOT_CONFIGURED"
    assert service.describe()["storage_operations_enabled"] is False
    assert service.health()["external_connection_verified"] is False

def test_category_record_requires_identity():
    record = CategoryRecord(record_id="sample", name="Sample")
    assert record.record_type == "MODEL_ROUTING"
