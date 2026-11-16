"""Offline tests for GLOBAL_INTEGRATIONS_STORAGE_ECOSYSTEM; no provider API calls."""
import json
from pathlib import Path

import pytest

from ..ecosystem_service import EcosystemService
from ..ecosystem_models import EcosystemRecord
from ..ecosystem_registry import EcosystemRegistry
from ..ecosystem_config import get_config, ECOSYSTEM_ID


PACKAGE_DIR = Path(__file__).resolve().parents[1]


def test_canonical_identity_and_foundation_health():
    service = EcosystemService()
    status = service.describe()
    health = service.health()
    assert status["ecosystem_id"] == "GLOBAL_INTEGRATIONS_STORAGE_ECOSYSTEM"
    assert status["package"] == "global_integrations_storage_ecosystem"
    assert health["success"] is True
    assert health["status"] == "FOUNDATION_READY"
    assert health["external_connections_verified"] is False
    assert health["storage_operations_enabled"] is False


def test_safe_defaults_are_disabled(monkeypatch):
    monkeypatch.delenv(f"{ECOSYSTEM_ID}_ENABLED", raising=False)
    config = get_config()
    assert config["enabled"] is False
    assert config["credentials_configured"] is False
    assert config["external_connection_state"] == "NOT_CONFIGURED"
    assert config["storage_operations_enabled"] is False


def test_manifest_matches_canonical_boundary():
    manifest = json.loads((PACKAGE_DIR / "ecosystem_manifest.json").read_text(encoding="utf-8"))
    result = EcosystemService().validate_manifest()
    assert result["valid"] is True
    assert all(result["checks"].values())
    assert manifest["taxonomy_only"] is True
    assert manifest["external_connection_state"] == "NOT_CONFIGURED"


def test_health_does_not_claim_provider_connection():
    result = EcosystemService().health()
    assert result["success"]
    assert not result["external_connections_verified"]
    assert result["storage_operations_enabled"] is False


def test_registry_duplicate_guard():
    registry = EcosystemRegistry()
    row = EcosystemRecord("sample-1", "SAMPLE", "Sample")
    registry.register(row)
    with pytest.raises(ValueError, match="DUPLICATE_RECORD_ID"):
        registry.register(row)


def test_record_requires_identity_fields():
    with pytest.raises(ValueError):
        EcosystemRecord("", "SAMPLE", "Sample")


def test_record_metadata_must_be_an_object():
    with pytest.raises(ValueError, match="metadata"):
        EcosystemRecord("sample-2", "SAMPLE", "Sample", metadata="not-an-object")
