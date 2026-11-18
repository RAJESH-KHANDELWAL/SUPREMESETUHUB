"""Offline foundation tests; no external AI provider calls."""
import pytest
from ..ecosystem_service import EcosystemService
from ..ecosystem_models import EcosystemRecord
from ..ecosystem_registry import EcosystemRegistry
def test_safe_health_contract():
    service=EcosystemService(); assert service.health()["external_connections_verified"] is False
    status=service.describe(); assert status["connection_state"]=="NOT_CONFIGURED" and status["storage_operations_enabled"] is False
def test_duplicate_guard():
    registry=EcosystemRegistry(); row=EcosystemRecord("one","SAMPLE","Sample"); registry.register(row)
    with pytest.raises(ValueError,match="DUPLICATE_RECORD_ID"): registry.register(row)
def test_identity_required():
    with pytest.raises(ValueError): EcosystemRecord("","SAMPLE","Sample")
