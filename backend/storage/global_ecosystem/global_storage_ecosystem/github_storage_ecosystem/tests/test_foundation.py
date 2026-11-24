"""Offline tests; these do not contact external provider APIs."""
import pytest
from ..ecosystem_service import EcosystemService
from ..ecosystem_models import EcosystemRecord
from ..ecosystem_registry import EcosystemRegistry
from ..ecosystem_taxonomy import list_ecosystems, find_ecosystem


def test_health_does_not_claim_provider_connection():
    result = EcosystemService().health()
    assert result['success']
    assert result['connection_state'] == 'NOT_CONFIGURED'
    assert not result['external_connections_verified']
    assert not result['storage_operations_enabled']


def test_taxonomy_and_category_index_are_consistent():
    rows = list_ecosystems()
    assert len(rows) == 30
    assert find_ecosystem('REPOSITORIES') is not None
    assert find_ecosystem('GITHUB_ISSUES_STORAGE_ECOSYSTEM') is not None


def test_registry_duplicate_guard():
    registry = EcosystemRegistry()
    row = EcosystemRecord('sample-1', 'SAMPLE', 'Sample')
    registry.register(row)
    with pytest.raises(ValueError, match='DUPLICATE_RECORD_ID'):
        registry.register(row)


def test_record_requires_identity_fields():
    with pytest.raises(ValueError):
        EcosystemRecord('', 'SAMPLE', 'Sample')
