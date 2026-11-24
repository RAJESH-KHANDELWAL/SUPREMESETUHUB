"""Offline tests for the ecosystem foundation."""
from ..ecosystem_service import EcosystemService
from ..ecosystem_models import EcosystemRecord
from ..ecosystem_registry import EcosystemRegistry

def test_health_does_not_claim_provider_connection():
    result = EcosystemService().health()
    assert result["success"] and not result["external_connections_verified"]

def test_registry_duplicate_guard():
    registry = EcosystemRegistry()
    row = EcosystemRecord("sample-1", "SAMPLE", "Sample")
    registry.register(row)
    try:
        registry.register(row)
    except ValueError as exc:
        assert str(exc) == "DUPLICATE_RECORD_ID"
    else:
        raise AssertionError("duplicate accepted")
