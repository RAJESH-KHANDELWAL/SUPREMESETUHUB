"""Offline foundation tests; no external provider API calls."""
import pytest
from ..ecosystem_service import EcosystemService
from ..ecosystem_models import EcosystemRecord
from ..ecosystem_registry import EcosystemRegistry
def test_health_does_not_claim_external_connection():
 service=EcosystemService();assert service.health()["external_connections_verified"] is False
 status=service.describe();assert status["connection_state"]=="NOT_CONFIGURED" and status["storage_operations_enabled"] is False
def test_registry_duplicate_guard():
 registry=EcosystemRegistry();row=EcosystemRecord("sample-1","SAMPLE","Sample");registry.register(row)
 with pytest.raises(ValueError,match="DUPLICATE_RECORD_ID"):registry.register(row)
def test_record_identity_required():
 with pytest.raises(ValueError):EcosystemRecord("","SAMPLE","Sample")
