"""Offline tests; these do not contact registrar or DNS provider APIs."""
import pytest
from ..ecosystem_service import EcosystemService
from ..ecosystem_models import EcosystemRecord
from ..ecosystem_registry import EcosystemRegistry
from ..service import GlobalDomainStorageEcosystem


def test_health_does_not_claim_provider_connection():
    result = EcosystemService().health()
    assert result['success']
    assert not result['external_connections_verified']


def test_registry_duplicate_guard():
    registry = EcosystemRegistry()
    row = EcosystemRecord('domain-1', 'DOMAIN', 'example.com')
    registry.register(row)
    with pytest.raises(ValueError, match='DUPLICATE_RECORD_ID'):
        registry.register(row)


def test_record_requires_identity_fields():
    with pytest.raises(ValueError):
        EcosystemRecord('', 'DOMAIN', 'example.com')


def test_domain_capabilities_are_metadata_only():
    result = GlobalDomainStorageEcosystem().describe()
    assert result['connection_status'] == 'not_configured'
    assert 'domain-registration-metadata' in result['capabilities']
