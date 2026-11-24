"""Offline foundation tests; no external Anthropic API calls are made."""
import pytest

from ..ecosystem_models import EcosystemRecord
from ..ecosystem_registry import EcosystemRegistry
from ..ecosystem_service import EcosystemService


def test_health_does_not_claim_live_connection():
    result = EcosystemService().health()
    assert result["success"] is True
    assert result["connection_state"] == "NOT_CONFIGURED"
    assert result["external_connections_verified"] is False


def test_registry_register_get_and_list():
    registry = EcosystemRegistry()
    record = EcosystemRecord("sample-1", "CATALOG_ITEM", "Sample")
    registry.register(record)
    assert registry.get("sample-1")["name"] == "Sample"
    assert len(registry.list()) == 1


def test_registry_rejects_duplicate_ids():
    registry = EcosystemRegistry()
    record = EcosystemRecord("sample-1", "CATALOG_ITEM", "Sample")
    registry.register(record)
    with pytest.raises(ValueError, match="DUPLICATE_RECORD_ID"):
        registry.register(record)


def test_record_requires_identity_fields():
    with pytest.raises(ValueError):
        EcosystemRecord("", "CATALOG_ITEM", "Sample")
