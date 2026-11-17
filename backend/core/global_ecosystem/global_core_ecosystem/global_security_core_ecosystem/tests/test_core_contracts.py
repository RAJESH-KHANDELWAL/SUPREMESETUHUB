"""Contract checks for the registered Global Security Core inventory."""
from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.domain_catalog import get_domains
from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.provider_catalog import get_provider_catalog
from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.policy import redact_sensitive_metadata


def test_security_taxonomy_and_provider_inventory():
    # The canonical catalog currently registers 33 domains and 6 providers.
    assert len(get_domains()) == 33
    assert len(get_provider_catalog()) == 6


def test_sensitive_metadata_is_redacted():
    assert redact_sensitive_metadata({"token": "hidden", "label": "safe"}) == {
        "label": "safe"
    }


def test_tenant_and_secret_contracts_reject_invalid_types():
    import pytest
    from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.contracts import (
        SecretReference,
        TenantContext,
    )

    with pytest.raises(ValueError, match="TENANT_ID_REQUIRED"):
        TenantContext(tenant_id=None, actor_id="actor").validate()
    with pytest.raises(ValueError, match="ACTOR_ID_REQUIRED"):
        TenantContext(tenant_id="tenant", actor_id=" ").validate()
    with pytest.raises(ValueError, match="SECRET_PROVIDER_REQUIRED"):
        SecretReference(provider=None, reference="vault/path")
    with pytest.raises(ValueError, match="SECRET_REFERENCE_REQUIRED"):
        SecretReference(provider="vault", reference=" ")
